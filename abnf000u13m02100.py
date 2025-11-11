## =====================================================
## [abnf000u13m02100.py] - Programação - Controle Diário
## =====================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13m02100_operacional_programacao_movimentacao_controle_diario ] //////////////////////////////////////////////////////////////////////////// #
# // Programação - Controle Diário.                                                                                                                      // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

'''
=====================================

Pendências:

[ok] Criar um td com informação das linhas-serviços que estão sem carro quando tirar um veiculo de um determinado horário.
     Esse aviso deve ser individual para cada um dos dois dias em analise
     Ainda falta fazer o teste abaixo:
     Desativar a geração automática e testar tirando o veiculo 32536 da linha 101-1
     Segundo Jean é para mais linhas serem influenciadas por isso

[ok] Criar grid individual para cada tipo de status de retenção.
    - 1 - Preso (cabeçalho vermelho)
    - 2 - Retorno diário (cabeçalho amarelo)
    - 3 - Retorno noturno (cabeçalho verde)
     Na tela de veículos retidos tem que aparecer a data e hora de agendamento.
     E também tem que ser ordenado por data e hora de agendamento.
     Pode remover a data/Hora da retenção pois este ja tem nos relatório e fica apenas poluindo a tela do usuário.

[ok] Criar um td com os veiculos que não estão sendo utilizados em cada uma das duas datas

[ok] Somente as retençoes de status 1 devem tirar o veículo da programação do dia.
     Somente as retençoes de status 1 devem atualizar o sistema para realocar veiculos

[ok] Na liberação de veiculos, somente as retençoes de status 1 devem atualizar o sistema para realocar veiculos

[ok] Somente as retençoes de status 1 podem não permitir que sejam retidos caso o sistema não esteja em modo automático.

[ok] O sistema deve reter veiculos somente que forem menor ou igual a data de agendamento.

[ok] Atualizar deve ser false porque tem a finalidade apenas de atualizar a tela do usuário.
     
[ok] Quando associar um veículo de 2 portas, em uma linha que no cadastro é 3, o sistema deve permitir mas trocar a mensagem.
     Mas isso somente quando o número de portas for menor que o padrão da linha.
     Com isso teremos duas mensagens de sucesso:
     - Alteração realizada com sucesso!
     - Alteração realizada com sucesso! No entanto, o veículo está com quantidade de portas fora do padrão da linha, por isso, deve ser substituído assim que possível!
     
[ok] O sistema tem que contar apenas um veiculos mesmo que este veículo tenha mais de uma retenção
     Alterar isso em tela
     
[ok] Na liberação de veículo mostrar o status de retenção e o GSD.

[ok] Pascoal do TCI.
     O veículo 12281 foi retirado da linha no dia de hoje.
     Ele não está retido pela manutenção.
     Então ele deveria constar em "Veículos não utilizados e não retidos com status 01 na data de hoje".
     Se agora 10:25 ele não está associado em linha nenhuma e nem na manutenção ele precisa aparecer nos disponíveis.

[ok] Problema na distruibuição dos veiculos.
     Entrando em Operacional/Cadastros/Prioridades de Linhas e tirando o relatório "Relação de prioridades cadastradas".
     Linha-serviço 412-1:
     Tem um registro principal com prioridade 176 com veiculo oficial 32855 mas sem subregistros anexados a ele.
     Linha-serviço 403-1:
     Tem um registro principal com prioridade 177 sem veiculo oficial mas tem subregistros anexados a ele.
     1 - 31347 - 31348 - 31349 - 31350 - 31351 - 31352 - 31353 - 31354
     2 - 31353 - 32800
     3 - 32807 - 32810 - 32811
     4 - 32834 - 32836
     5 - 31335
     6 - 12273 - 12274 - 12275 - 12276 - 12277 - 12279 - 12280 - 12284 - 12294 - 12297 - 12298 - 12307 - 12312
     Analisando o dia de amanhã.
     O Jean inseriu o veículo 31353 na linha 403-1 para vermos como se comporta.
     Deu certo o processo acima e a linha e funcionaou o processo de locação de veículos na linha 403-1.
     Sendo assim ficou definido que, no momento, não vamos mexer no processo atual de distruibuição dos veículos nas linhas-serviços.
     Atualmente, somente a linha 412-1 não recebe um veículo pelo fato de não sair da garagem, mas isto não esta sendo um problema.

[ok] Novo relatório para Karolin => STATUS DIÁRIO DA MANUTENÇÂO
     Feito filtros com data e hora
     E checkbox nos status
     
[ok] Relatórios 1,2 e 3 é aquela programação da frota, na soltura fica uma pessoa na portaria dando baixa nos veículos que vão saindo. 
     Essa pessoa tem um relatório na mão com todas as saídas indexado por horário.
     Então teria que ser o relatório 2 mas classificado pelo horário da saída.
     Jean ficou de conversar com a galera da manhã pra saber as colunas necessárias, mas é tudo que já tem nos relatórios 1,2 e 3.
     Em conversa com Jean dia 04/09/2025, ficou definido que esse relatório não vai atender a portaria pela falta da informação do motorista.

[ok] Mudanças na estrutura de status.
     O status 3 vai passar a ser 4 e o 2 passar a ser 3.
     Vai ser criado um novo status 2 chamado RETIDO tanto o status 1 quanto o 2 vão funcionar do mesmo jeito bloqueando e removendo veiculos do dia seguinte.
     A partir da meia noite, tudo o que tiver aberto de status 2, 3 e 4 vão ser fechados automaticamente antes da alocação do dia seguinte.
    
[ok] Grids da tela inicial
     Mudar os dados apresentados nos grids da tela inicial
     Regra do Grid 01:
     Vamos tratar cada linha-serviço independente do veiculo oficial 
     Os campos mantem os mesmos mas os dados a serem apresentado serão baseados em regras
     Não vai ter mais o processo de ficar procurando a primeira viagem após saída da garagem
     O sistema deve mostrar sempre a proxima viagem de cada linha-serviço basedo no horário atual
     Regras:
     1) Linha que o horário atual esta maior que o ultimo horário de chegada dessa linha
        Essa linha não deve mais aparecer na tela
     2) Linha que o horário atual esta menor que o ultimo horário de chegada dessa linha
        Aparecer o ultimo horário de saída dessa linha antes do horário atual
     3) Linha que o horário atual esta menor que o primeiro horário de saída dessa linha
        Aparecer o primeiro horário dessa linha que ainda não foi feito
     Regra do Grid 02:
     Vamos buscar todas as viagens inciais de cada veiculo geral
     Então nem todas as linhas vão aparecer saindo da garagem
     E também linhas que não são a primeira do veículo oficial também não vão aparecer no grid
     
[ok] Em conversa com o Jean, ficou definido que o modo para saber se uma linha-serviço esta sem veículo vai ter que mudar
     Ele não poder ser igual do veiculo disponivel usando o horário local porque corre o risco de sumir o aviso antes do operador acertar o problema
     Então ficou definido da seguinte forma.
     O sistema vai varrer todos os horários pelos veiculos gerais e horarios
     Quando encontrar horarios sem veiculos vai guardando as linhas-serviços até encontrar um horário que tenha veiculo
     Se encontrar limpa a memória e começa o processo tudo de novo
     Se chegar ao final com algo na memoria então isso deve ser mostrado na tela principal
     [14:16, 08/09/2025] RSP-Jean (Planejamento): Acontece assim, por questões de operação muitas vezes uma linha que encerra no TCI 19h por exemplo o fiscal segura
     esse ônibus lá. A última viagem seria 19:00 as 19:20 do TCI para a Garagem, essa viagem o fiscal retira o veículo e utiliza ele como reserva em outra linha.
     A viagem de 19:00 as 19:20 ficou sem realizar, aí lá pras 21h 22h liberou algum veículo, aí ele coloca para realizar a viagem que ficou pendente mesmo em atraso.
     [14:17, 08/09/2025] RSP-Jean (Planejamento): Resumindo, teria a possibilidade do alerta ficar ativo quando se tratar da última viagem?
     
[ok] Relatório 01, 02 e 03
     Realizar alterações de visualização para caber mais informações por folha
     [ok] a) Remover os campos "Tipo de registro" e "Motivo"
     [ok] b) Cabeçalho "Veiculo escalado" mudar para "Veic"
     [ok] c) Cabeçalho "Observação" mudar para "Obs"
     [ok] d) Cabeçalho "Tipo dia" mudar para "TD"
     [ok] e) Cabeçalho "Partida" mudar para "Hor"
     [ok] f) Cabeçalho "Sentido" mudar para "S"
     [ok] g) Alterar "VEICULO TITULAR" e "VEICULO SUBSTITUTO" para "TIT" e "SUB"
     [ok] h) Colocar apenas a primeira letra do tipo de dia: U, S, D...
     [ok] i) Colocar apenas a primeira letro no sentido: I, V
     [ok] j) No campo "Origem" colocar apenas as 30 primeiras letras
     [ok] k) Na frente de veiculo deixar uma coluna em branco com espaço de 6 letras
     
[ok] Karolin: Temos mais dois ajustes que vamos precisar no controle de frota
     um é cadastrar as vans de apoio
     35058/ S.O.S - 35062 e a van 57
     e o outro é que precisamos poder prender as vans (todas elas, inclusive as do elevar) sem elas entrarem nessa conta
     Em conversa com a Karolin dia 10/09/2025, ela disse que todos os veículos estão aparecendo no sistema para poderem ser retidos

[ok] Nos relatorios 01 a 05, criar três setores virtuais chamados "reserva" e "manutenção" e "externo".
     Ele devem conter os veículos que estiverem nessa situação.
     Então os veículos saem no relatório juntamente com os outros que tem setores oficiais.
     Essas analises deve ser feitas pelo veiculo geral para ver a rota do veículo em toda sua jornada
     # SETOR XXX  => Aquilo que sai da garagem e ja tem seu setor definido 
     # RESERVA    => O que não está associado a nenhuma linha e nem retido pela manutenção
     # MANUTENÇÃO => Veículos que estão retidos pela manutenção com status 01 e 02
     # EXTERNO    => Quando a primeira viagem do veículo geral for fora da garagem

[ok] Inserir novos motivos de troca:
     RETORNO PARA LINHA TITULAR
     TROCA NA SOLTURA
     TROCA DE CARRO NA OPERACAO
     VEICULO ENCERROU PRIMEIRO TURNO NA GARAGEM
     VEICULO DISPONIVEL PARA SOLTURA
     
[ok] Relatório 06
     Ele vai ter dois formatos criando o relatorio 06 e 07
     06 - DIARIO POR LINHA SERVIÇO - GERAL
     07 - DIARIO POR LINHA SERVIÇO - TEMPO REAL
     O 06 mantém como esta atualmente
     O 07 deve apresentar somente a proxima viagem de cada linha-serviço basedo no horário atual
     Mesmo que você peça uma data diferente da data atual, o relatório vai sempre se basear na hora atual
     Dessa forma você pode saber como foi ou como vai ser qualquer período baseado no horário atual
     Em conversa com o Jean dia 12/09, essa pendência foi cancelada porque agora as informações em tempo real estão no grid 1

[ok] Criar usuário para:
     ROMULO DA SILVA MARTINEZ
     E avisar o Mathus e a Karolin

[ok] Criar usuários e avisar Matheus e a Karolin
     PAULO ALBERTO POPPI
     GERARDO FERREIRA LIMA FILHO
     EVAIR SAMPAIO DE OLIVEIRA
     ANTONIO JOSE DE SOUSA FERREIRA
     JULIANA DUARTE LOPES
     CRISTIANO MATHEUS FERREIRA DOS SANTOS
     
[ok] Colocar uma senha na tela de "cancelar e refazer o diario"
     Colocar a liberação por grupo e não mais por usuário
     Dessa forma não será mais necessário criar um grupo individual para Jean, Julia e Meneses
     Aproveitar para testar os eventos JS: onkeydown, onkeyup e onkeypress para criar uma nova tela de senha
     
[ok] Criar uma tabela de motivos para substituição de veículos.
     Precisa definir se esse campo será obrigatórios.
     E também o campo de observação se vai continuar sendo obrigatório.
     Criar uma planilha para abastecer os registros orfãos
     01 - ACERTO DE HORARIO                  
     02 - MARKETING / ADESIVACAO             
     03 - OCORRENCIA                         
     04 - QUEBRA                             
     05 - RETIRADO PARA SUBSTITUIR OUTRA LINHA
     06 - TROCA PARA ABASTECIMENTO           
     07 - VEICULOS EXTERNOS                  
     08 - VEICULOS PEDIDOS (MANUTENCAO)      
     09 - VEICULOS PEDIDOS (TI PARA COLETAS) 
     99 - OUTROS
     A planilha totalizou 304 registros a serem arrumados.
     Passei a planilha para o Jean em 03/09/2025 e estou aguardando ele devolver para eu acertar os registros.

[ok] Criar usuário para o Galvão: FERNANDO GALVAO PELLINI
     Criar um perfil chamado "FERNANDO GALVAO"
     
[ok] Karolin - 19/09/2025
     No relatório, colocar datas individuais para cada status e tratar isso no relatório 11
     
[ok] Criar uma rotina para poder definir qual data vai ser alterada nos registros
     Ao passar pela primeira tela tenha um botão "data de hoje", "data de amanha" e um terceiro onde o usuário define a data
     Dessa forma da pra utilizar o mesmo programa que temos hoje apenas passando a data por parâmetro em memória

[  ] Criar uma rotina para o Jean pode cancelar registros de substituição de veículos
     Essa rotina deve ter uma tela que informa que os veículos originais não voltam a sua posição anterior a transferência portanto necessida correções manuais
     Mudar estrutura das tabelas que estão autorizando procedimentos
     Atualmente a tabela "abnf_operacional_cadastro_grupos_usuarios_vinculos" tem o campo "perrefd" que permite refazer os registros de diário
     Ver possibilidade disse campo deve ser passado para a tabela "abnf_operacional_cadastro_grupos_usuarios" abaixo do campo "permaut"
     Dessa forma a autorização passa a ser do grupo e não mais por usuário
     Conversar com o Jean possibilidade de ele, Julinha e Meneses ficarem em um grupo separado do CCO lembrando que eles não poderão liberar veiculos retidos pelo CCO

[  ] Karolin conversou com CCO para definir acréscimos na lista GSD.
     CCO vai passar lista para para colocar na lista de GSD do SIGOM.
     Também deixar o campo obrigatório para toda retenção que for realizada.
     Quando o campo for obrigatório, fazer um estudo dos registros que ficaram sem GSD para analisar a viabilidade de completar as informações.

[  ] Criar mais uma rotina no sistema para retenção de veiculos em lote.
     Vai ter um botão na tela principal chamado "Retenção de veículo em lote".
     Ao clicar nesse botão o usuário vai poder selecionar quais veiculos serão retidos e informar o motivo.
     Isso será muito útil para o CCO fazer retenções de veículos que não podem ser deixados como reserva no fim de semana.
     Nesses casos ele retem o veiculo para aquele dia com status 02 para que ele seja automaticamente liberado.
     Mas para isso é necessário que o GSD do CCO esteja devidamente definido no sistema.
     
[  ] Nos relatórios que envolve a oficia:
     Ativar os filtros de veiculos, GSD e status de retenção
     
[  ] Testar dois usuarios acessando o sistema quando ele estiver gerando o dia posterior

[  ] Ver porque meu usuário esta conseguindo "Desativar a escala automática"
     Testar com usuario do Uilson para saber o que ele consegue fazer também
     
[  ] Cria um novo programa de cadastro de veículos
     Esse novo programa vai ter classificação de veiculos com checkbox: operação, elevar, passeio, sos, van, etc
     Criar também classificações que indicam quais dias da semana esses veículos vão poder ficar como "reserva"
     Assim que tiver esses classificações na semana, ver com Jean quais relatórios devem analisar esses parâmetros e alterar.

=====================================

mysqldump -u flexgb -pFlexGB#Server#1961#001 gb001 > /flexgb/abnfbkp/gb001.sql

http://10.0.0.10:8005/rapidosumarepiracicaba
http://172.16.11.92:8005/rapidosumarepiracicaba

http://189.44.98.122:8905/rapidosumarepiracicaba

<a href="https://www.google.com" target="_blank" rel="noopener noreferrer">
    Visitar Google em Nova Aba
</a>

Veículo reservas:
 
12273
12274
12275
12276
12277
12279
12280
12284
12294
12297
12298
12307
12312
31335
32806
32807
32810
32834
32836
57017 

=====================================
'''

def abnf000u13m02100_operacional_programacao_movimentacao_controle_diario(dabnfopg, balocvei = False):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13m02100_operacional_programacao_movimentacao_controle_diario(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '13M02101A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        ddatahoj = abnf_converte_data(date.today())
        ddataama = abnf_converte_data(abnf_soma_dias_data(date.today(), 1))
        sauxi001 = '<font color=white size=5>Linhas-serviços de: </font><font color=cyan FACE="Courier New" size=5><b>' + ddatahoj + '</b></font>'
        sauxi001 = sauxi001 + '<font color=white size=5> ás </font><font color=cyan FACE="Courier New" size=5><b>' + abnf_websocket_date_time(4) + '</b></font>'
        sauxi002 = '<font color=white size=5>Linhas-serviços de: </font><font color=cyan FACE="Courier New" size=5><b>' + ddataama + '</b></font>'
        lnewpage = [
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
            ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
                ('tr-0', 'text-white bg-secondary', False),
                    ('td-0', None, 2, None, 1, None, None),
                        ('legend-0', 'Programação - Controle Diário'),
                        ('div-1', 'sdivulat'), ('div-9', None),
                    ('td-9', None),
                ('tr-9', None),
                ('tr-0', None, False),
                    ('td-0', None, None, None, None, None, None),
                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
                                # ///////////////////////
                                # Linhas-serviços de hoje
                                # ///////////////////////
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 1, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'text-white bg-secondary', False),
                                    ('td-0', None, 1, None, 1, None, None), ('label-0', sauxi001, 'form-control-label'), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 1, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None), ('div-1', 'sdivthoj'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # ///////////////////////////////////
                                # Linhas-serviços sem veículo de hoje
                                # ///////////////////////////////////
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None), ('div-9', None), ('div-1', 'sdivthsv'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # ///////////////////////////////////////////////////////////////////
                                # Veículos não utilizados e não retidos com status 01 na data de hoje
                                # ///////////////////////////////////////////////////////////////////
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None), ('div-9', None), ('div-1', 'sdivthvn'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # /////////////////////////
                                # Linhas-serviços de amanhã
                                # /////////////////////////
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 1, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'text-white bg-secondary', False),
                                    ('td-0', None, 1, None, 1, None, None), ('label-0', sauxi002, 'form-control-label'), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 1, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None), ('div-1', 'sdivtama'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # /////////////////////////////////////
                                # Linhas-serviços sem veículo de amanhã
                                # /////////////////////////////////////
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None), ('div-1', 'sdivtasv'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # /////////////////////////////////////////////////////////////////////
                                # Veículos não utilizados e não retidos com status 01 na data de amanhã
                                # /////////////////////////////////////////////////////////////////////
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None), ('div-9', None), ('div-1', 'sdivtavn'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # ////////////////////////////////////////////////
                                # Modo da geração automática de escala de veículos
                                # ////////////////////////////////////////////////
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None), ('div-1', 'sdivtaut'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # //////
                                # Botões
                                # //////
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None),
                                        ('table-0', None),
                                            ('tr-0', None, False),
                                                ('td-0', None, 1, None, 0, None, None),
                                                    ('alt255-0', 2),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),
                                                    ('button-0', 'btatuinx', 'btn btn-primary mt-1', 'Atualizar informações'),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),
                                                    ('alt255-0', 2),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),
                                                    ('button-0', 'btrelatx', 'btn btn-primary mt-1', 'Relatórios'),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),
                                                    ('alt255-0', 2),
                                                ('td-9', None),
                                            ('tr-9', None),
                                        ('table-9', None),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None),
                                        ('alt255-0', 2),
                                        ('button-1', 'btdesesx', 'btn btn-primary mt-1', 'Desativar a escala de veículos automática do dia de hoje', 'Salvar Registro', 'btdesesc', 'btn btn-primary mt-2', 'Confirmar a desativação', 'Confirma a paralização da análise automática para o dia de hoje?'),
                                        ('alt255-0', 2),
                                        ('button-0', 'btcandia', 'btn btn-primary mt-1', 'Cancelar e refazer o diário de ' + ddataama),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 0, None, None),
                                        ('table-0', 'table table-bordered table-sm table-responsive'),
                                            ('tr-0', None, False),
                                                ('td-0', None, 1, None, 1, 1, None),
                                                    ('button-0', 'btalthoj', 'btn btn-primary mt-1', 'Alterar informações de ' + ddatahoj),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),
                                                    ('alt255-0', 1),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),
                                                    ('button-0', 'btaltama', 'btn btn-primary mt-1', 'Alterar informações de ' + ddataama),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 1, 1, None),
                                                    ('alt255-0', 1),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 2, 1, None),
                                                    ('label-0',  'Data:', 'form-control-label'),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 1, 1, None),
                                                    ('alt255-0', 1),
                                                ('td-9', None),                
                                                ('td-0', None, 1, None, 1, 1, None),
                                                    ('date-0',   'ddataesp', 'form-control', '16px', None, 'btaltesp', True, 0, None),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 1, 1, None),
                                                    ('alt255-0', 1),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 1, 1, None),
                                                    ('button-0', 'btaltesp', 'btn btn-primary mt-1', 'Alterar informações'),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 1, 1, None),
                                                    ('alt255-0', 1),
                                                ('td-9', None),
                                                ('td-0', None, 1, None, 1, 1, None),
                                                    ('button-0', 'btcanalt', 'btn btn-primary mt-1', 'Cancelar alterações'),
                                                ('td-9', None),
                                            ('tr-9', None),
                                        ('table-9', None),
                                    ('td-9', None),
                                ('tr-9', None),
                            ('table-9', None),
                        ('form-9', None),
                    ('td-9', None),
                ('tr-9', None),
                ('tr-0', None, False),
                    ('td-0', None, None, None, None, None, None),
                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
                                # ////////////////////////////////////
                                # Veículos retidos - Status 01 - Preso
                                # ////////////////////////////////////
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 3, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'bg-danger', False),
                                    ('td-1', 'text-white', 1, None, 1, None, None, 200), ('label-0', '<font color=white size=5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>', 'form-control-label'), ('td-9', None),
                                    ('td-0', 'text-white bg-secondary', 1, None, 1, None, None), ('label-0', '<font color=white size=5>Veículos retidos - Status 01 - Preso</font>', 'form-control-label'), ('td-9', None),
                                    ('td-1', 'text-white', 1, None, 1, None, None, 200), ('label-0', '<font color=white size=5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>', 'form-control-label'), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 3, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 3, None, 0, None, None), ('div-1', 'sdivtvr1'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 2, None, 0, None, None), ('font-0', 'Courier New;', '16px', None, 'Total de veículos retidos:'), ('td-9', None),
                                    ('td-0', None, 1, None, 1, None, None), ('div-1', 'sdivttv1'), ('font-0', 'Courier New;', '16px', None, '0'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # /////////////////////////////////////
                                # Veículos retidos - Status 02 - Retido
                                # /////////////////////////////////////
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 3, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'bg-abnf001', False),
                                    ('td-1', 'text-white', 1, None, 1, None, None, 200), ('label-0', '<font color=white size=5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>', 'form-control-label'), ('td-9', None),
                                    ('td-0', 'text-white bg-secondary', 1, None, 1, None, None), ('label-0', '<font color=white size=5>Veículos retidos - Status 02 - Retido</font>', 'form-control-label'), ('td-9', None),
                                    ('td-1', 'text-white', 1, None, 1, None, None, 200), ('label-0', '<font color=white size=5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>', 'form-control-label'), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 3, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 3, None, 0, None, None), ('div-1', 'sdivtvr2'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 2, None, 0, None, None), ('font-0', 'Courier New;', '16px', None, 'Total de veículos retidos:'), ('td-9', None),
                                    ('td-0', None, 1, None, 1, None, None), ('div-1', 'sdivttv2'), ('font-0', 'Courier New;', '16px', None, '0'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # /////////////////////////////////////////////
                                # Veículos retidos - Status 03 - Retorno diário
                                # /////////////////////////////////////////////
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 3, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'bg-warning', False),
                                    ('td-1', 'text-white', 1, None, 1, None, None, 200), ('label-0', '<font color=white size=5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>', 'form-control-label'), ('td-9', None),
                                    ('td-0', 'text-white bg-secondary', 1, None, 1, None, None), ('label-0', '<font color=white size=5>Veículos retidos - Status 03 - Retorno diário</font>', 'form-control-label'), ('td-9', None),
                                    ('td-1', 'text-white', 1, None, 1, None, None, 200), ('label-0', '<font color=white size=5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>', 'form-control-label'), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 3, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 3, None, 0, None, None), ('div-1', 'sdivtvr3'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 2, None, 0, None, None), ('font-0', 'Courier New;', '16px', None, 'Total de veículos retidos:'), ('td-9', None),
                                    ('td-0', None, 1, None, 1, None, None), ('div-1', 'sdivttv3'), ('font-0', 'Courier New;', '16px', None, '0'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # //////////////////////////////////////////////
                                # Veículos retidos - Status 04 - Retorno noturno
                                # //////////////////////////////////////////////
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 3, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'bg-success', False),
                                    ('td-1', 'text-white', 1, None, 1, None, None, 200), ('label-0', '<font color=white size=5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>', 'form-control-label'), ('td-9', None),
                                    ('td-0', 'text-white bg-secondary', 1, None, 1, None, None), ('label-0', '<font color=white size=5>Veículos retidos - Status 04 - Retorno noturno</font>', 'form-control-label'), ('td-9', None),
                                    ('td-1', 'text-white', 1, None, 1, None, None, 200), ('label-0', '<font color=white size=5>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</font>', 'form-control-label'), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', 'text-white text-white bg-dark', False),
                                    ('td-0', None, 3, None, None, None, None),
                                        ('font-0', 'Courier New;', '20px', None, ''),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 3, None, 0, None, None), ('div-1', 'sdivtvr4'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 2, None, 0, None, None), ('font-0', 'Courier New;', '16px', None, 'Total de veículos retidos:'), ('td-9', None),
                                    ('td-0', None, 1, None, 1, None, None), ('div-1', 'sdivttv4'), ('font-0', 'Courier New;', '16px', None, '0'), ('div-9', None), ('td-9', None),
                                ('tr-9', None),
                                # //////
                                # Botões
                                # //////
                                ('tr-0', None, False),
                                    ('td-0', None, 3, None, 0, None, None),
                                        ('alt255-0', 2),
                                        ('button-0', 'btatuiny', 'btn btn-primary mt-1', 'Atualizar informações'),
                                        ('alt255-0', 2),
                                        ('button-0', 'btrelaty', 'btn btn-primary mt-1', 'Relatórios'),
                                        ('alt255-0', 2),
                                        ('button-0', 'btretvei', 'btn btn-primary mt-1', 'Reter veículo'),
                                        ('alt255-0', 2),
                                        ('button-0', 'btlibvei', 'btn btn-primary mt-1', 'Liberar veículo'),
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
        # //////////////////////////////////
        # Desabilita todos os botões do form
        # //////////////////////////////////
        lbuttfor = ['btatuinx', 'btrelatx', 'btdesesx', 'btcandia', 'btalthoj', 'btaltama', 'btaltesp', 'btcanalt', 'btatuiny', 'btrelaty', 'btretvei', 'btlibvei']
        for sauxi001 in lbuttfor:
            abnf_socket_004([10, sauxi001])     # Desabilita o botão 
        # /////////////////////////////////////////////////////////
        # Mantem o sistema parado enquanto tiver tendo atualizações
        # /////////////////////////////////////////////////////////
        sarqdown = "abnftmp/abnf000u13m02100.now"
        bvalidad = True
        while os.path.isfile(sarqdown):
            if bvalidad:
                abnf_alert('Aguarde! Atualizando informações...', 5)
                bvalidad = False
            time.sleep(1)
        abnf000u13m02103_operacional_programacao_movimentacao_controle_diario(icodbase, sabnproj, dglobaux, iidfilia, balocvei)
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13m02101_operacional_programacao_movimentacao_controle_diario ] //////////////////////////////////////////////////////////////////////////// #
# // Programação - Controle Diário.                                                                                                                      // #
# // Form de inclusão/alteração/exclusão do registro principal de prioridade.                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13m02101_operacional_programacao_movimentacao_controle_diario(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13m02101_operacional_programacao_movimentacao_controle_diario(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        iidusuar = dglobaux['iidusuar']
        if dabnfopg['abnfobj0'] in (['btatuinx', 'btatuinx'], ['btatuiny', 'btatuiny']):    
            # /////////////////////
            # Atualizar informações
            # /////////////////////
            abnf000u13m02103_operacional_programacao_movimentacao_controle_diario(icodbase, sabnproj, dglobaux, iidfilia, False)
        elif dabnfopg['abnfobj0'] in (['btrelatx', 'btrelatx'], ['btrelaty', 'btrelaty']):
            # //////////
            # Relatórios
            # //////////
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13M02102A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            # //////////////////////////
            # Buscas em tabelas externas
            # //////////////////////////
            lrelator = ([
                [ 0, ''],
                [ 1, '01 - SAÍDA DE GARAGEM - GERAL'],
                [ 2, '02 - SAÍDA DE GARAGEM - VEÍCULOS COM SETORES'],
                [ 3, '03 - SAÍDA DE GARAGEM - VEÍCULOS SEM SETORES'],
                [ 4, '04 - SAÍDA DE GARAGEM - VEÍCULOS POR SETORES'],
                [ 5, '05 - SAÍDA DE GARAGEM - SETORES POR VEÍCULOS'],
                [ 6, '06 - DIARIO POR LINHA-SERVIÇO'],
                [ 7, '07 - DIARIO POR VEÍCULO'],
                [ 8, '08 - SUBSTITUÍÇÃO DE VEÍCULOS'],
                [ 9, '09 - VEÍCULOS NÃO UTILIZADOS E VEÍCULOS RETIDOS'],
                [10, '10 - RETENÇÃO E LIBERAÇÃO DE VEÍCULOS'],
                [11, '11 - DIÁRIO DA MANUTENÇÃO'],
                # [12, '12 - STATUS DIÁRIO DA MANUTENÇÃO - MODELO 02'],
            ])
            lidveicu = abnf_database_menu(icodbase, iidfilia, 'L', '0201', 3, 2, 0)
            lidsdede = abnf_database_sqlx(icodbase, 'L', '12008A', 2, (iidfilia, 'A','A','A'))
            lformrel = [(1, 'HTML')] # , (2, 'CSV')]
            # /// #
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('table-0', 'table table-bordered table-sm table-responsive'),
                    ('tr-0', 'text-white bg-secondary', False),
                        ('td-0', None, 2, None, 1, None, None),
                            ('legend-0', 'Programação - Relatórios'),
                        ('td-9', None),
                    ('tr-9', None),
                    ('tr-0', None, False),
                        ('td-0', None, None, None, None, None, None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                ('tr-0', None, False),              
                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Relatório', 'form-control-label'),                                                      ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                    ('td-0', None, 4, None, 0, None, None),                ('select-1', 'irelator', 'form-control', '16px', 'ddataini', lrelator, 1, None, False, '13M021A'),   ('td-9', None),
                                ('tr-9', None), 
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Data-hora inicial', 'form-control-label'),                                              ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('date-0',   'ddataini', 'form-control', '16px', None, 'hhoraini', True, 0, None),                   ('td-9', None),
                                    ('td-1', None, 1, None, 0, None, None, 20),            ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                    ('td-1', None, 1, None, 0, None, None, 100),           ('time-1', 'hhoraini', 'form-control', '16px', '00:00', 'ddatafim', True, 0, None),                  ('td-9', None),
                                    ('td-1', None, 1, None, 0, None, None, 550),           ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Data-hora final', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('date-0',   'ddatafim', 'form-control', '16px', None, 'hhorafim', True, 0, None),                   ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('time-1', 'hhorafim', 'form-control', '16px', '23:59', 'iidveicu', True, 0, None),                  ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Veículo', 'form-control-label'),                                                        ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                    ('td-0', None, 4, None, 0, None, None),                ('select-0', 'iidveicu', 'form-control', '16px', 'iidsdede', lidveicu, 1, None, False),              ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'GSD', 'form-control-label'),                                                            ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                    ('td-0', None, 4, None, 0, None, None),                ('select-0', 'iidsdede', 'form-control', '16px', 'iformrel', lidsdede, 1, None, False),              ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Status de retenção', 'form-control-label'),                                             ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                    ('td-0', None, 4, None, None, None, None),
                                        ('table-0', 'table table-bordered table-sm table-responsive'),
                                            ('tr-0', None, False),
                                                ('td-0', None, 3, None, None, None, None), ('font-0', 'Courier New;', '15px', None, 'Status&nbsp;01&nbsp;-&nbsp;Preso'),                        ('td-9', None),
                                                ('td-0', None, 1, None, 1, None, None),    ('checkbox-0', 'bstatu01', 1, 1, 'Courier New', '15px', 'b', 'P', None), 
                                                ('td-0', None, 1, None, 0, None, None),    ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('date-0',   'ddats01i', 'form-control', '16px', None, 'ddats01f', True, 0, None),                   ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('date-0',   'ddats01f', 'form-control', '16px', None, 'ddats02i', True, 0, None),                   ('td-9', None),
                                                ('td-9', None),
                                            ('tr-9', None),
                                            ('tr-0', None, False),
                                                ('td-0', None, 3, None, None, None, None), ('font-0', 'Courier New;', '15px', None, 'Status&nbsp;02&nbsp;-&nbsp;Retido'),                       ('td-9', None),
                                                ('td-0', None, 1, None, 1, None, None),    ('checkbox-0', 'bstatu02', 1, 1, 'Courier New', '15px', 'b', 'P', None),                             ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('date-0',   'ddats02i', 'form-control', '16px', None, 'ddats02f', True, 0, None),                   ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('date-0',   'ddats02f', 'form-control', '16px', None, 'ddats03i', True, 0, None),                   ('td-9', None),
                                            ('tr-9', None),
                                            ('tr-0', None, False),
                                                ('td-0', None, 3, None, None, None, None), ('font-0', 'Courier New;', '15px', None, 'Status&nbsp;03&nbsp;-&nbsp;Retorno&nbsp;diário'),          ('td-9', None),
                                                ('td-0', None, 1, None, 1, None, None),    ('checkbox-0', 'bstatu03', 1, 1, 'Courier New', '15px', 'b', 'P', None),                             ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('date-0',   'ddats03i', 'form-control', '16px', None, 'ddats03f', True, 0, None),                   ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('date-0',   'ddats03f', 'form-control', '16px', None, 'ddats04i', True, 0, None),                   ('td-9', None),
                                            ('tr-9', None),
                                            ('tr-0', None, False),
                                                ('td-0', None, 3, None, None, None, None), ('font-0', 'Courier New;', '15px', None, 'Status&nbsp;04&nbsp;-&nbsp;Retorno&nbsp;noturno'),         ('td-9', None),
                                                ('td-0', None, 1, None, 1, None, None),    ('checkbox-0', 'bstatu04', 1, 1, 'Courier New', '15px', 'b', 'P', None),                             ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('date-0',   'ddats04i', 'form-control', '16px', None, 'ddats04f', True, 0, None),                   ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                                ('td-0', None, 1, None, 0, None, None),    ('date-0',   'ddats04f', 'form-control', '16px', None, 'btgerrel', True, 0, None),                   ('td-9', None),
                                            ('tr-9', None),
                                        ('table-9', None),
                                    ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Formato do relatório', 'form-control-label'),                                           ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                                         ('td-9', None),
                                    ('td-0', None, 4, None, 0, None, None),                ('select-0', 'iformrel', 'form-control', '16px', 'btgerrel', lformrel, 1, None, False),              ('td-9', None),
                                ('tr-9', None),
                                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                ('table-0', None),
                                    ('tr-0', None, False),
                                        ('td-0', None, 1, None, 1, None, None),
                                            ('button-0', 'btgerrel', 'btn btn-primary mt-2', 'Gerar relatório'),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                        ('td-0', 'table-active', 1, None, 1, None, None), 
                                            ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Cancelar'),
                                        ('td-9', None),
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
        elif dabnfopg['abnfobj0'] == ['btretvei', 'btretvei']:
            # ///////////////////
            # Retenção de veículo
            # ///////////////////
            lauxi001 = abnf_database_sqlx(icodbase, 'X', '13021A', 0, (iidfilia, iidusuar))
            if lauxi001 == [] or lauxi001[0][3] != 'A' or lauxi001[0][4] != 'A':
                abnf_alert('Seu usuário não tem permissão para realizar este procedimento!', 5)
                abnf_socket_004([5, 'btretvei'])
            else:
                abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13M02102A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                sdescusg = lauxi001[0][1] + ' (' + str(lauxi001[0][2]) + ')'
                # //////////////////////////
                # Buscas em tabelas externas
                # //////////////////////////
                lidveicu = abnf_database_menu(icodbase, iidfilia, 'L', '0201', 1, 2, 0)
                lstatret = abnf_personal_retorna_lista(13002)
                lidsdede = abnf_database_sqlx(icodbase, 'L', '12008A', 1, (iidfilia, 'A','A','A'))
                # /// #
                lnewpage = [
                    ('div-0', 'container', None, None),
                    ('hr-0', None),
                    ('div-0', 'row', None, None),
                    ('div-0', 'col d-flex justify-content-center', None, None),
                    ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                    ('table-0', 'table table-bordered table-sm table-responsive'),
                        ('tr-0', 'text-white bg-secondary', False),
                            ('td-0', None, 2, None, 1, None, None),
                                ('legend-0', 'Programação - Retenção de Veículo'),
                            ('td-9', None),
                        ('tr-9', None),
                        ('tr-0', None, False),
                            ('td-0', None, None, None, None, None, None),
                                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                ('table-0', 'table table-bordered table-sm table-responsive'),
                                    ('tr-0', None, False),
                                        ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Grupo solicitante', 'form-control-label'),                                   ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                              ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', sdescusg),                                    ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Veículo solicitado', 'form-control-label'),                                  ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                              ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('select-0', 'iidveicu', 'form-control', '16px', 'ddataage', lidveicu, 1, None, False),   ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Data do agendamento', 'form-control-label'),                                 ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                              ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('date-0',  'ddataage', 'form-control', '16px', None, 'hseghage', True, 0, None),         ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Horário do agendamento', 'form-control-label'),                              ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                              ('td-9', None),
                                        ('td-0', None, 6, None, 0, None, None),                ('time-1', 'hseghage', 'form-control', '16px', '00:00', 'sdescrre', True, 0, None),       ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Motivo da retenção', 'form-control-label'),                                  ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                              ('td-9', None),
                                        ('td-0', None, 3, None, 0, None, None),                ('textarea-0', 'sdescrre', 'form-control', 2, 1000, '16px', None, 'istatret'),            ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Status da retenção', 'form-control-label'),                                  ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                              ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('select-0', 'istatret', 'form-control', '16px', 'iidsdede', lstatret, 1, None, False),   ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'GSD (opcional)', 'form-control-label'),                                      ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                              ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),                ('select-0', 'iidsdede', 'form-control', '16px', 'btretvex', lidsdede, 1, None, False),   ('td-9', None),
                                    ('tr-9', None),
                                    ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                    ('table-0', None),
                                        ('tr-0', None, False),
                                            ('td-0', None, 1, None, 1, None, None),
                                                ('button-1', 'btretvex', 'btn btn-primary mt-2', 'Reter o veículo', 'Salvar Registro', 'btretvei', 'btn btn-primary mt-2', 'Salvar', 'Confirma a retenção do veículo?'),
                                            ('td-9', None),
                                            ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                            ('td-0', 'table-active', 1, None, 1, None, None), 
                                                ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Cancelar'),
                                            ('td-9', None),
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
        elif dabnfopg['abnfobj0'] == ['btlibvei', 'btlibvei']:
            # //////////////////////
            # Liberar veículo retido
            # //////////////////////
            lmfields = [
                ['iidoprrv', 'radio', 'Nenhum veículo retido foi selecionado para poder ser liberado', ['Notnull', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btlibvei')
            if bvalidad:
                iidoprrv = lmfields[0][4]
                lauxi001 = abnf_database_sqlx(icodbase, 'X', '13021A', 0, (iidfilia, iidusuar))
                if lauxi001 == [] or lauxi001[0][3] != 'A' or lauxi001[0][4] != 'A':
                    abnf_alert('Seu usuário não tem permissão para realizar este procedimento!', 5)
                    abnf_socket_004([5, 'btlibvei'])
                else:
                    # ///////////////////////////////////////
                    # Busca o registro de retenção do veículo
                    # ///////////////////////////////////////
                    sauxi001 = 'SELECT '
                    # Campos das tabelas
                    sauxi001 = sauxi001 + 'abnf02.prefvei, '    # [00] Prefixo do veículo
                    sauxi001 = sauxi001 + 'abnf02.placave, '    # [01] Placa do veículo
                    sauxi001 = sauxi001 + 'abnf01.codctrl, '    # [02] Código de controle
                    sauxi001 = sauxi001 + 'abnf01.dataage, '    # [03] Data do agendamento
                    sauxi001 = sauxi001 + 'abnf01.seghage, '    # [04] Hora do agendamento
                    sauxi001 = sauxi001 + 'abnf01.descrre, '    # [05] Motivo da retenção
                    sauxi001 = sauxi001 + 'abnf01.statret, '    # [06] Status da retenção
                    sauxi001 = sauxi001 + 'abnf01.idsdede, '    # [07] ID da definicao de GSD do SIGOM
                    sauxi001 = sauxi001 + 'abnf07.dessdeg, '    # [08] Descricao do grupo de GSD
                    sauxi001 = sauxi001 + 'abnf07.codsdeg, '    # [09] Codigo do grupo de GSD
                    sauxi001 = sauxi001 + 'abnf06.dessdes, '    # [10] Descrição do subgrupo de GSD
                    sauxi001 = sauxi001 + 'abnf06.codsdes, '    # [11] Codigo do subgrupo de GSD
                    sauxi001 = sauxi001 + 'abnf05.dessded, '    # [12] Descrição da definição de GSD
                    sauxi001 = sauxi001 + 'abnf05.codsded, '    # [13] Codigo da definição de GSD
                    sauxi001 = sauxi001 + 'abnf01.dtreten, '    # [14] Data/hora da retenção do veículo                    
                    sauxi001 = sauxi001 + 'abnf01.idcusgr, '    # [15] ID do grupo que reteve
                    sauxi001 = sauxi001 + 'abnf04.nomeusu, '    # [16] Nome do usuário que reteve
                    sauxi001 = sauxi001 + 'abnf03.descusg, '    # [17] Nome do grupo que reteve
                    sauxi001 = sauxi001 + 'abnf03.codcusg, '    # [18] Código grupo que reteve
                    sauxi001 = sauxi001 + 'abnf01.situreg, '    # [19] Situação do registro de veículo
                    sauxi001 = sauxi001 + 'abnf01.idfilia, '    # [20] ID da Filial
                    sauxi001 = sauxi001 + 'abnf01.dtliber  '    # [21] Data/hora de liberação
                    # Tabela de retenção
                    sauxi001 = sauxi001 + 'FROM       abnf_operacional_movimentacao_programacao_retencao_veiculos AS abnf01 '
                    # Tabela de veículos
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos                                      AS abnf02 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                    # Tabela de grupo de usuários
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_grupos_usuarios                   AS abnf03 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idcusgr = abnf03.idcusgr '
                    # Tabela de usuários (usuário que reteve)
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_sistema_usuarios                                       AS abnf04 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idcusre = abnf04.idusuar '
                    # Tabela definição de GSD
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_sigom_cadastro_defeitos_definicoes                     AS abnf05 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idsdede = abnf05.idsdede '
                    # Tabela de subgrupos de GSD
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_sigom_cadastro_defeitos_subgrupos                      AS abnf06 '
                    sauxi001 = sauxi001 + 'ON         abnf05.idsdesg = abnf06.idsdesg '
                    # Tabela de grupo de GSD
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_sigom_cadastro_defeitos_grupos                         AS abnf07 '
                    sauxi001 = sauxi001 + 'ON         abnf06.idsdegr = abnf07.idsdegr '
                    # Cláusula WHERE
                    # Condições SQL
                    sauxi001 = sauxi001 + 'WHERE '
                    sauxi001 = sauxi001 + 'abnf01.idfilia = ' + str(iidfilia) + ' AND ' # ==> Somente registros da filial
                    sauxi001 = sauxi001 + 'abnf01.situreg != "C" AND '                  # ==> Somente registros não cancelados (retenção)
                    sauxi001 = sauxi001 + 'abnf01.idoprrv = ' + str(iidoprrv) + ';'     # ==> Buscando o registro da retenção
                    # Execução
                    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                    # Debug (início)
                    # abnf_show('05', lsqlre01, 1)
                    # abnf_show('06', lauxi001, 1)
                    # Debug (fim)
                    # ///////////////////////////////////
                    # Abastece a tela de veículos retidos
                    # ///////////////////////////////////
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('Registro de retenção de veículo não encontrado! Entre em contato com o depto. de sistemas!', 4)
                        abnf_socket_004([5, 'btlibvei'])
                    else:
                        sprefvei = lsqlre01[0][0] + ' (' + lsqlre01[0][1] + ')'
                        scodctrl = str(1000000 + lsqlre01[0][2])[1:]
                        sdataage = abnf_converte_data(lsqlre01[0][3])
                        hseghage = abnf_converte_segundos_em_hora_string(lsqlre01[0][4], False)
                        sdescrre = lsqlre01[0][5]
                        sstatret = abnf_personal_retorna_string(13002, lsqlre01[0][6])
                        iidsdede = lsqlre01[0][7]
                        ddtreten = abnf_converte_datahora(lsqlre01[0][14], 0)
                        iidcusgr = lsqlre01[0][15]
                        snomeusu = lsqlre01[0][16]
                        sdescusg = lsqlre01[0][17] + ' (' + str(lsqlre01[0][18]) + ')'
                        ssitureg = lsqlre01[0][19]
                        iidfilix = lsqlre01[0][20]
                        ddtliber = lsqlre01[0][21]
                        if ssitureg != 'A':
                            abnf_alert('Este registro de retenção não pode ser aberto porque não está mais ativo!', 5)
                            abnf_socket_004([5, 'btlibvei'])
                        elif iidfilix != iidfilia:
                            abnf_alert('Este registro de retenção não pode ser aberto porque não pertence a esta filial!', 5)
                            abnf_socket_004([5, 'btlibvei'])
                        elif ddtliber != None:
                            abnf_alert('Este registro de retenção não pode ser aberto porque ja foi liberado!', 5)
                            abnf_socket_004([5, 'btlibvei'])
                        elif iidcusgr != lauxi001[0][0]:
                            abnf_alert('Este registro de retenção não pode ser liberado porque não pertence ao seu grupo de usuário!', 5)
                            abnf_socket_004([5, 'btlibvei'])
                        else:
                            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13M02102A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidoprrv', iidoprrv),)])      # ==> Guardado dados do registro de retenção do veículo para a próxima função. Obs: tem que ter essa vírgula: "),)])"
                            # /// #
                            lnewpage = [
                                ('div-0', 'container', None, None),
                                ('hr-0', None),
                                ('div-0', 'row', None, None),
                                ('div-0', 'col d-flex justify-content-center', None, None),
                                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                                ('table-0', 'table table-bordered table-sm table-responsive'),
                                    ('tr-0', 'text-white bg-secondary', False),
                                        ('td-0', None, 2, None, 1, None, None),
                                            ('legend-0', 'Programação - Liberação de Veículo Retido'),
                                        ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', None, None, None, None, None, None),
                                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                                ('tr-0', 'text-white text-white bg-dark', False),
                                                    ('td-0', None, 3, None, None, None, None),
                                                        ('font-0', 'Courier New;', '20px', None, ''),
                                                    ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Veículo', 'form-control-label'),                   ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', sprefvei),          ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Controle', 'form-control-label'),                  ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', scodctrl),          ('td-9', None),
                                                ('tr-9', None),                                                
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Data do agendamento', 'form-control-label'),       ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', sdataage),          ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Hora do agendamento', 'form-control-label'),       ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', hseghage),          ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', 'text-white text-white bg-dark', False),
                                                    ('td-0', None, 3, None, None, None, None),
                                                        ('font-0', 'Courier New;', '20px', None, ''),
                                                    ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Motivo da retenção', 'form-control-label'),        ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', sdescrre),          ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Status da retenção', 'form-control-label'),        ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', sstatret),          ('td-9', None),
                                                ('tr-9', None),
                            ]
                            if iidsdede > 0:
                                sauxi001 = lsqlre01[0][8] + ' (' + str(lsqlre01[0][9]) + ') - ' + lsqlre01[0][10] + ' (' + str(lsqlre01[0][11]) + ') - ' + lsqlre01[0][12] + ' (' + str(lsqlre01[0][13]) + ')'
                                lnewpage = lnewpage + [
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'GSD', 'form-control-label'),                       ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', sauxi001),          ('td-9', None),
                                                ('tr-9', None),
                                ]
                            lnewpage = lnewpage + [
                                                ('tr-0', 'text-white text-white bg-dark', False),
                                                    ('td-0', None, 3, None, None, None, None),
                                                        ('font-0', 'Courier New;', '20px', None, ''),
                                                    ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Data/Hora da retenção', 'form-control-label'),     ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', ddtreten),          ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Usuário que reteve', 'form-control-label'),        ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', snomeusu),          ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-1', 'table-active', 1, None, 0, None, None, 300), ('label-0', 'Grupo que reteve', 'form-control-label'),          ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('font-0', 'Courier New;', '16px', 'brown', sdescusg),          ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', 'text-white text-white bg-dark', False),
                                                    ('td-0', None, 3, None, None, None, None),
                                                        ('font-0', 'Courier New;', '20px', None, ''),
                                                    ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Descrição adicional de liberação (opcional)', 'form-control-label'),       ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                            ('td-9', None),
                                                    ('td-0', None, 3, None, 0, None, None),                ('textarea-0', 'sdescrli', 'form-control', 2, 1000, '16px', None, 'btlibvex'),          ('td-9', None),
                                                ('tr-9', None),
                                                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                                ('table-0', None),
                                                    ('tr-0', None, False),
                                                        ('td-0', None, 1, None, 1, None, None),
                                                            ('button-1', 'btlibvex', 'btn btn-primary mt-2', 'Liberar o veículo', 'Salvar Registro', 'btlibvei', 'btn btn-primary mt-2', 'Salvar', 'Confirma a liberação do veículo?'),
                                                        ('td-9', None),
                                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                                        ('td-0', 'table-active', 1, None, 1, None, None), 
                                                            ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Cancelar'),
                                                        ('td-9', None),
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
        elif dabnfopg['abnfobj0'] == ['btdesesc', 'btdesesc']:
            # ////////////////////////////////////////////////////
            # Parar a escala de veículos automática do dia de hoje
            # ////////////////////////////////////////////////////
            lauxi001 = abnf_database_sqlx(icodbase, 'X', '13021A', 0, (iidfilia, iidusuar))
            if lauxi001 == [] or lauxi001[0][3] != 'A' or lauxi001[0][4] != 'A' or not lauxi001[0][5]:
                abnf_alert('Seu usuário não tem permissão para realizar este procedimento!', 5)
                abnf_socket_004([5, dabnfopg['abnfobj0'][0]])
            else:
                # //////////////////////////////////////////////////////////////////////////////////////////
                # Busca o último registro de automação para saber se o sistema ainda esta em modo automático
                # //////////////////////////////////////////////////////////////////////////////////////////
                sauxi001 = 'SELECT defmeto FROM abnf_operacional_movimentacao_programacao_automacao WHERE situreg != "C" ORDER BY dtmetod DESC LIMIT 1;'
                lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                if lsqlre01 == [] or (iqtdre01 > 0 and lsqlre01[0][0] == 'M'):
                    abnf_alert('Preocesso não realizado devido ao sistema não estar mais em modo automático!', 5)
                    abnf_socket_004([5, 'btdesesx'])
                else:
                    # //////////////////////////////////////////////////////////////////////////
                    # Gera um registro de automação que libera o sistema para operar manualmente
                    # //////////////////////////////////////////////////////////////////////////
                    bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_movimentacao_programacao_automacao', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                    [
                        ('dtmetod', 'CURRENT_TIMESTAMP'),
                        ('defmeto', 'M'),
                        ('idfilia', iidfilia),
                        ('situreg', 'A'),
                    ])
                    if bvalidad:
                        lauxi001 = ('A geração automática de escala de veículos esta desativada!', 'white', 'danger')
                        lnewpage = [
                            ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
                                ('tr-0', 'text-white bg-' + lauxi001[2] , False),
                                    ('td-0', None, 1, None, 1, None, None),
                                        ('font-0', 'Courier New;', '20px', lauxi001[1], lauxi001[0]),
                                    ('td-9', None),
                                ('tr-9', None),
                            ('table-9', None),
                        ]
                        snewpage = abnf_create_page(lnewpage)
                        abnf_socket_004([1, 'sdivtaut', snewpage])
                        abnf_alert('Sistema alterado para modo manual de escala de veículos!', 3)
                    else:
                        abnf_alert('Erro ao criar registros de automação de programação! Entre em contato com o depto. de sistemas!', 4)
        elif dabnfopg['abnfobj0'] == ['btcandia', 'btcandia']:
            # ///////////////////////////
            # Cancelar a refazer o diário
            # ///////////////////////////
            lauxi001 = abnf_database_sqlx(icodbase, 'X', '13021A', 0, (iidfilia, iidusuar))
            if lauxi001 == [] or lauxi001[0][3] != 'A' or lauxi001[0][4] != 'A' or not lauxi001[0][6]:
                abnf_alert('Seu usuário não tem permissão para realizar este procedimento!', 5)
                abnf_socket_004([5, 'btcandia'])
            else:
                # Debug (início)
                # abnf_show('06', lauxi001, 1)
                # Debug (fim)
                abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13M02102A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                ddataama = abnf_soma_dias_data(date.today(), 1)
                sauxi001 = '<font color=white size=5>Programação - Cancelar e refazer o diário de: ' + '</font>'
                sauxi001 = sauxi001 +'<font color=cyan FACE="Courier New" size=5><b>' + abnf_converte_data(ddataama) + '</b></font>'
                sauxi002 = 'Este processo exclui toda a programação (tanto automática quanto manual) realizada para a data informada acima. '
                sauxi002 = sauxi002 + 'Portanto ele deve ser feito somente em casos de ter alterações na OSO que compõe a data informada.'
                # /// #
                lnewpage = [
                    ('div-0', 'container', None, None),
                    ('hr-0', None),
                    ('div-0', 'row', None, None),
                    ('div-0', 'col d-flex justify-content-center', None, None),
                    ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                    ('table-0', 'table table-bordered table-sm table-responsive'),
                        ('tr-0', 'text-white bg-secondary', False),
                            ('tr-0', 'text-white bg-secondary', False),
                                ('td-0', None, 10, None, 1, None, None), ('label-0', sauxi001, 'form-control-label'), ('td-9', None),
                            ('tr-9', None), 
                        ('tr-9', None),
                        ('tr-0', None, False),
                            ('td-0', None, None, None, None, None, None),
                                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                ('table-0', 'table table-bordered table-sm table-responsive'),
                                    ('tr-0', None, False),
                                        ('td-0', None, 3, None, 1, None, None), ('font-0', 'Courier New;', '25px', 'brown', 'Atenção!'), ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', None, 3, None, 0, None, None), ('font-0', 'Courier New;', '20px', 'black', sauxi002), ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Senha para liberação do processo:', 'form-control-label'),            ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                       ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),           ('input-0', 'ssenhpro', 'form-control', 0, 20, '16px', None, 'btcanrex', True, 0), ('td-9', None),
                                    ('tr-9', None),
                                    ('table-0', None),
                                        ('tr-0', None, False),
                                            ('td-0', None, 1, None, 1, None, None),
                                                ('button-1', 'btcanrex', 'btn btn-primary mt-2', 'Refazer o diário do dia '+ abnf_converte_data(ddataama),
                                                'Refazer o diário', 'btcanref', 'btn btn-primary mt-2', 'Confirmar', 'Refazer o diário do dia '+ abnf_converte_data(ddataama) + '?'),
                                            ('td-9', None),
                                            ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                            ('td-0', 'table-active', 1, None, 1, None, None), 
                                                ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Abortar o cancelamento'),
                                            ('td-9', None),
                                        ('tr-9', None),
                                    ('table-9', None),
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
        elif dabnfopg['abnfobj0'] in (['btalthoj', 'btalthoj'], ['btaltama', 'btaltama'], ['btaltesp', 'btaltesp']):
            # ////////////////////////////////////////////
            # Alterações em registros de hoje ou de amanhã
            # ////////////////////////////////////////////
            lauxi001 = abnf_database_sqlx(icodbase, 'X', '13021A', 0, (iidfilia, iidusuar))
            if lauxi001 == [] or lauxi001[0][3] != 'A' or lauxi001[0][4] != 'A' or not lauxi001[0][5]:
                abnf_alert('Seu usuário não tem permissão para realizar este procedimento!', 5)
                abnf_socket_004([5, dabnfopg['abnfobj0'][0]])
            else:
                if dabnfopg['abnfobj0'] == ['btaltesp', 'btaltesp']:
                    lmfields = [
                        ['ddataesp', 'date', 'F', 'data a ser alterada', ['Notnull', 'D', 'Return_date', '<today'], None],
                    ]
                    bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btaltesp')
                    if bvalidad:
                        # Debug (início)
                        # abnf_show('05', lmfields[0][5], 0)
                        # Debug (fim)
                        ldataaux = [lmfields[0][5], 'S']
                else:
                    if   dabnfopg['abnfobj0'] == ['btalthoj', 'btalthoj']: ldataaux = [date.today(), 'H']
                    elif dabnfopg['abnfobj0'] == ['btaltama', 'btaltama']: ldataaux = [abnf_soma_dias_data(date.today(), 1), 'A']
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('ddataaux', ldataaux[0]),)])      # ==> Guardado dados da data a ser mostrada para a próxima função. Obs: tem que ter essa vírgula: "),)])"
                    bvalidad = False
                    if ldataaux[1] == 'H':      # Alterar informações de hoje
                        bvalidad = True
                    elif ldataaux[1] == 'A':    # Alterar informações de amanhã
                        # ////////////////////////////////////////////////////////////////////////////////
                        # Busca o último registro de automação para saber se o sistema esta em modo manual
                        # ////////////////////////////////////////////////////////////////////////////////
                        sauxi001 = 'SELECT defmeto FROM abnf_operacional_movimentacao_programacao_automacao WHERE situreg != "C" ORDER BY dtmetod DESC LIMIT 1;'
                        lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                        if lsqlre01 == [] or (iqtdre01 > 0 and lsqlre01[0][0] == 'M'):
                            bvalidad = True
                        if not bvalidad:
                            abnf_alert('Não é permitido alterações em registros de ' + abnf_converte_data(ldataaux[0]) + ' devido ao sistema ainda estar em análise automática!', 5)
                            abnf_socket_004([5, 'btaltama'])
                # //////////////////////////////////////////////////////////////
                # Monta a tela com os registros referêntes a data correspondente
                # //////////////////////////////////////////////////////////////
                if bvalidad:
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13M02102A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                    # //////////////////////////////////////////////////////////////////////////////
                    # Dados de linhas-serviços-horário-sentido-veículo-origem da data correspondente
                    # //////////////////////////////////////////////////////////////////////////////
                    sauxi001 = 'SELECT '
                    # Campos das tabelas
                    sauxi001 = sauxi001 + 'abnf02.idoprdi, '    # [00] ID do registro de diário de programação
                    sauxi001 = sauxi001 + 'abnf04.prefvei, '    # [01] Prefixo do veículo
                    sauxi001 = sauxi001 + 'abnf02.seghini, '    # [02] Horário de início (em segundos)
                    sauxi001 = sauxi001 + 'abnf02.sentido, '    # [03] Sentido
                    sauxi001 = sauxi001 + 'abnf01.codolin, '    # [04] Codigo da linha
                    sauxi001 = sauxi001 + 'abnf02.veicpro, '    # [05] Veículo-Serviço
                    sauxi001 = sauxi001 + 'abnf03.desoloc  '    # [06] Descrição do local de origem
                    # Tabelas SQL
                    sauxi001 = sauxi001 + 'FROM       abnf_operacional_cadastro_linhas                 AS abnf01 '
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_programacao_diario AS abnf02 '
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_locais                 AS abnf03 '
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_cadastro_veiculos                           AS abnf04 '
                    sauxi001 = sauxi001 + 'ON         abnf02.idveicu = abnf04.idveicu '
                    sauxi001 = sauxi001 + 'AND        abnf04.situreg != "C" '                   # ==> Somente registros não cancelados (veículos)
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_operacional_cadastro_setor_veiculos         AS abnf05 '
                    sauxi001 = sauxi001 + 'ON         abnf02.idosetv = abnf05.idosetv '
                    sauxi001 = sauxi001 + 'AND        abnf05.situreg != "C" '                   # ==> Somente registros não cancelados (setores)        
                    # Condições SQL
                    sauxi001 = sauxi001 + 'WHERE abnf01.idolinh = abnf02.idolinh '              # ==> Chave join dos registros
                    sauxi001 = sauxi001 + 'AND   abnf02.idolori = abnf03.idoloca '              # ==> Chave join dos registros
                    # Condições SQL
                    sauxi001 = sauxi001 + 'AND   abnf01.situreg = "A" '                         # ==> Somente registros ativos (linhas)
                    sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                        # ==> Somente registros não cancelados (diário)
                    sauxi001 = sauxi001 + 'AND   abnf02.idfilia = ' + str(iidfilia) + ' '       # ==> Somente registros da filial
                    sauxi001 = sauxi001 + 'AND   abnf02.dataope = "' + str(ldataaux[0]) + '" '  # ==> Somente registros da data correspondente
                    # Ordenação
                    sauxi001 = sauxi001 + 'ORDER BY abnf04.prefvei, abnf02.seghini, abnf02.sentido, abnf01.codolin, abnf02.veicpro;'
                    # Execução
                    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                    # Debug (início)
                    # abnf_show('05', sauxi001, 0)
                    # abnf_show('06', lsqlre01, 1)
                    # Debug (fim)
                    lidoprdi = [(0, '')]
                    for lauxi001 in lsqlre01:
                        sprefvei = str(lauxi001[1]) if lauxi001[1] != None else '[SEM VEICULO]'
                        lidoprdi.append((
                            lauxi001[0],
                            'VEÍCULO: ' + sprefvei + ' - ' +
                            'HOR-SEN: ' + abnf_converte_segundos_em_hora_string(lauxi001[2], False) + '-' + str(lauxi001[3]) + ' - ' +
                            'LIN-SER: ' + str(lauxi001[4]) + '-' + str(lauxi001[5]) + ' - ' +
                            'ORIGEM: ' + str(lauxi001[6])
                        ))
                    lidveicu = abnf_database_menu(icodbase, iidfilia, 'L', '0201', 1, 2, 0)
                    lidveicu.insert(1, (-1, 'REMOVER VEÍCULO'))
                    lidomsub = abnf_database_menu(icodbase, iidfilia, 'L', '1306', 1, 2, 2)
                    sauxi001 = '<font color=white size=5>Programação - Alterar informações de: ' + '</font>'
                    sauxi001 = sauxi001 +'<font color=cyan FACE="Courier New" size=5><b>' + abnf_converte_data(ldataaux[0]) + '</b></font>'
                    lnewpage = [
                        ('div-0', 'container', None, None),
                        ('hr-0', None),
                        ('div-0', 'row', None, None),
                        ('div-0', 'col d-flex justify-content-center', None, None),
                        ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                        ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
                            ('tr-0', 'text-white bg-secondary', False),
                                ('td-0', None, 2, None, 1, None, None),
                                    ('label-0', sauxi001, 'form-control-label'),
                                ('td-9', None),
                            ('tr-9', None),
                            ('tr-0', None, False),
                                ('td-0', None, None, None, None, None, None),
                                    ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                        ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
                                            ('tr-0', None, False),
                                                ('td-0', None, None, None, None, None, None),
                                                    ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                                    ('table-0', 'table table-bordered table-sm table-responsive'),
                                                        ('tr-0', None, False),
                                                            ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0',  'Registro', 'form-control-label'),                                         ('td-9', None),
                                                            ('td-0', None, 1, None, 0, None, None),                ('label-0',  '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                            ('td-0', None, 3, None, 0, None, None),                ('select-0', 'iidoprdi', 'form-control', '16px', 'iidveicu', lidoprdi, 1, None, False), ('td-9', None),
                                                            ('td-0', None, 1, None, 0, None, None),                ('label-0',  '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                        ('tr-9', None),
                                                        ('tr-0', None, False),
                                                            ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0',  'Veículo', 'form-control-label'),                                          ('td-9', None),
                                                            ('td-0', None, 1, None, 0, None, None),                ('label-0',  '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                            ('td-0', None, 3, None, 0, None, None),                ('select-0', 'iidveicu', 'form-control', '16px', 'iidomsub', lidveicu, 1, None, False), ('td-9', None),
                                                            ('td-0', None, 1, None, 0, None, None),                ('label-0',  '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                        ('tr-9', None),
                                                        ('tr-0', None, False),
                                                            ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0',  'Motivo', 'form-control-label'),                                           ('td-9', None),
                                                            ('td-0', None, 1, None, 0, None, None),                ('label-0',  '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                            ('td-0', None, 3, None, 0, None, None),                ('select-0', 'iidomsub', 'form-control', '16px', 'smotisub', lidomsub, 1, None, False), ('td-9', None),
                                                            ('td-0', None, 1, None, 0, None, None),                ('label-0',  '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                        ('tr-9', None),
                                                        ('tr-0', None, False),
                                                            ('td-0', 'table-active', 1, None, 0, None, None),      ('label-0', 'Complemento', 'form-control-label'),                                       ('td-9', None),
                                                            ('td-0', None, 1, None, 0, None, None),                ('label-0', '&nbsp;', 'form-control-label'),                                            ('td-9', None),
                                                            ('td-0', None, 3, None, 0, None, None),                ('textarea-0', 'smotisub', 'form-control', 2, 1000, '16px', None, 'btalterx'),          ('td-9', None),
                                                            ('td-0', None, 1, None, 0, None, None),                ('label-0',  '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                        ('tr-9', None),
                                                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                                        ('table-0', None),
                                                            ('tr-0', None, False),
                                                                ('td-0', None, 1, None, 0, None, None),
                                                                    ('button-1', 'btalterx', 'btn btn-primary mt-1', 'Salvar as alterações', 'Salvar Registro', 'btaltera', 'btn btn-primary mt-2', 'Salvar', 'Confirma a gravação das alterações?'),
                                                                    ('alt255-0', 2),
                                                                    ('button-0', 'btcancel', 'btn btn-primary mt-1', 'Cancelar'),
                                                                ('td-9', None),
                                                            ('tr-9', None),
                                                        ('table-9', None),
                                                        ('form-9', None),
                                                    ('table-9', None),
                                                    ('form-9', None),
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
        elif dabnfopg['abnfobj0'] == ['btcanalt', 'btcanalt']:
            # /////////////////////////
            # Cancelamento de alteração
            # /////////////////////////
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13M02102A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
                    ('tr-0', 'text-white bg-secondary', False),
                        ('td-0', None, 2, None, 1, None, None),
                            ('legend-0', 'Programação - Cancelamento de alteração'),
                        ('td-9', None),
                    ('tr-9', None),
                    ('tr-0', None, False),
                        ('td-0', None, None, None, None, None, None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
                                    ('tr-0', None, False),
                                        ('td-0', None, None, None, None, None, None),
                                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0',  'Registro de alteração', 'form-control-label'),                            ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0',  '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('number-0', 'iidoprsu', 'form-control', 0, 10, '16px', None, 'ssenhpro', True, None),  ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0',  '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Senha para liberação do processo:', 'form-control-label'),                ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                           ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('input-0', 'ssenhpro', 'form-control', 0, 20, '16px', None, 'btcanalx', True, 0),     ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0',  '&nbsp;', 'form-control-label'),                                          ('td-9', None),
                                                ('tr-9', None),
                                                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                                ('table-0', None),
                                                    ('tr-0', None, False),
                                                        ('td-0', None, 1, None, 0, None, None),
                                                            ('button-1', 'btcanalx', 'btn btn-primary mt-1', 'Cancelamento da alteração', 'Cancelar a alteração', 'btcanalt', 'btn btn-primary mt-2', 'Confirmar', 'Confirma o cancelamento da alteração definida?'),
                                                            ('alt255-0', 2),
                                                            ('button-0', 'btcancel', 'btn btn-primary mt-1', 'Abortar o cancelamento'),
                                                        ('td-9', None),
                                                    ('tr-9', None),
                                                ('table-9', None),
                                                ('form-9', None),
                                            ('table-9', None),
                                            ('form-9', None),
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
           
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13m02102_operacional_programacao_movimentacao_controle_diario ] //////////////////////////////////////////////////////////////////////////// #
# // Programação - Controle Diário.                                                                                                                      // #
# // Ações da tela principal do controle diário.                                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13m02102_operacional_programacao_movimentacao_controle_diario(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13m02102_operacional_programacao_movimentacao_controle_diario(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        iidusuar = dglobaux['iidusuar']
        # ////////////////////////////////////////////
        # Desabilita todos os botões de todos os forms
        # ////////////////////////////////////////////
        lbuttfor = ['btretvex', 'btlibvex', 'btcanrex', 'btalterx', 'btcancel']
        for sauxi001 in lbuttfor:
            abnf_socket_004([10, sauxi001])     # Desabilita o botão 
        # /////////////////////////////////////////////////////////
        # Mantem o sistema parado enquanto tiver tendo atualizações
        # /////////////////////////////////////////////////////////
        sarqdown = "abnftmp/abnf000u13m02100.now"
        bvalidad = True
        while os.path.isfile(sarqdown):
            if bvalidad:
                abnf_alert('Aguarde! Atualizando informações...', 5)
                bvalidad = False
            time.sleep(1)
        # ///////////////
        # Ações dos forms
        # ///////////////
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:
            # //////////////////////////
            # Voltar para tela principal
            # //////////////////////////
            abnf000u13m02100_operacional_programacao_movimentacao_controle_diario(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btcanref', 'btcanref']:
            if os.path.isfile(sarqdown):
                abnf_alert('Registros de diário de programação sendo atualizados neste momento! Por favor tente novamente em alguns instantes...', 5)
                abnf_socket_004([5, 'btcanref'])
            else:
                # ///////////////////////////
                # Cancelar e refazer o diário
                # ///////////////////////////
                lmfields = [
                    ['ssenhpro', 'input', 'F', 'senha para liberação do processo', ['Notnull', 'P'], None],
                ]
                bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btcanref')
                if bvalidad:
                    # Debug: (inicio)
                    # abnf_show('10', lmfields, 1)
                    # Debug: (fim)
                    ssenhpro = lmfields[0][5]
                    if ssenhpro != 'A6N3S9G1':  # *** Senha ***
                        abnf_alert('Senha inválida!', 4)
                        abnf_socket_004([5, 'btcanref'])
                        bvalidad = False
                if bvalidad:
                    ddataama = abnf_soma_dias_data(date.today(), 1)
                    lcamposb = ('idoprdi', None)
                    lfilbusc = (('idfilia', '=', iidfilia), ('dataope', '=', ddataama), ('situreg', '!=', 'C'))
                    lorderby = ('dataope', 'idolinh', 'veicpro')
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_diario', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] and iqtdre01 == 0:
                        abnf_alert('Não foram encontrados registros a serem cancelados na data ' + abnf_converte_data(ddataama) + '!', 5)
                        abnf_socket_004([5, 'btcanref'])
                    else:
                        # /////////////////////////////////////
                        # Cria o arquivo temporário de bloqueio
                        # /////////////////////////////////////
                        with open(sarqdown, 'w') as sarquwri:
                            sarquwri.write('Atualizando registros de diário de programação...' + '\n')
                            sarquwri.write(str(dglobaux['slogiusu']) + '\n')                    
                        # //////////////////////
                        # Excluindo os registros
                        # //////////////////////
                        abnf_alert('Aguarde! Excluindo registros de programação diária...', 15)
                        abnf_socket_004([10, 'btcanrex'])     # Desabilita o botão
                        abnf_socket_004([10, 'btcancel'])     # Desabilita o botão
                        icontreg = 0
                        for lauxi001 in lsqlre01:
                            iidoprdi = lauxi001[0]
                            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_movimentacao_programacao_diario', iidoprdi, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                            if bvalidad:
                                icontreg += 1
                            else:
                                abnf_alert('Erro ao excluir registros de diário! Entre em contato com o depto. de sistemas!', 4)
                                break
                        # ///////////////////////////////////////
                        # Exclui o arquivo temporário de bloqueio
                        # ///////////////////////////////////////
                        try:
                            os.remove(sarqdown)
                        except:
                            pass
                        if os.path.isfile(sarqdown):
                            abnf_alert('Erro ao excluir o arquivo de bloqueio! Entre em contato com o depto. de sistemas!', 4)
                        else:
                            if bvalidad:
                                abnf_alert(str(icontreg) + ' registro' + ('s' if icontreg != 1 else '') + ' de programação diária excluído' + ('s' if icontreg != 1 else '') + ' com sucesso!', 3)
                                time.sleep(3)
                                abnf000u13m02100_operacional_programacao_movimentacao_controle_diario(dabnfopg, True)
        elif dabnfopg['abnfobj0'] == ['btretvei', 'btretvei']:
            # /////////////
            # Reter veículo
            # /////////////
            lmfields = [
                ['iidveicu', 'select',   'M', 'veículo',                ['Notnull', 'D', 'Return_integer'],         None],
                ['ddataage', 'date',     'F', 'data do agendamento',    ['Notnull', 'D', 'Return_date', '>=today'], None],
                ['hseghage', 'time-0',   'M', 'horário do agendamento', ['Notnull', 'D'],                           None],
                ['sdescrre', 'textarea', 'M', 'motivo da retenção',     ['Notnull', 'P'],                           None],
                ['istatret', 'select',   'M', 'status da retenção',     ['Notnull', 'D', 'Return_integer'],         None],
                ['iidsdede', 'select',   'M', 'GSD',                    ['Return_integer', 'Empty_to_zero'],        None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btretvei')
            if bvalidad:
                # Debug: (inicio)
                # abnf_show('10', lmfields, 1)
                # Debug: (fim)
                iidveicu = lmfields[0][5]
                ddataage = lmfields[1][5]
                hseghage = lmfields[2][5]
                sdescrre = lmfields[3][5]
                istatret = lmfields[4][5]
                iidsdede = lmfields[5][5]
                # //////////////////
                # Buscando o veículo
                # //////////////////
                lcamposb = ('situreg', 'idfilia', 'prefvei')
                lfilbusc = (('idveicu', '=', iidveicu), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('Veículo não encontrado! Entre em contato com o depto. de sistemas!', 4)
                    abnf_socket_004([5, 'btretvei'])
                elif lsqlre01[0][0] != 'A':
                    abnf_alert('O veículo solicitado não esta ativo!', 5)
                    abnf_socket_004([5, 'btretvei'])
                elif lsqlre01[0][1] != iidfilia:
                    abnf_alert('O veículo solicitado não pertence a esta filial!', 5)
                    abnf_socket_004([5, 'btretvei'])
                else:
                    sprefvei = lsqlre01[0][2]
                    # ///////////////////////////////////////////////////////////////////////////////////////////////////
                    # Busca o último registro de automação para saber se o sistema esta em modo manual
                    # Caso esteja então não pode aceitar a retenção do veículo se ele estiver alocado para o dia seguinte
                    # Isso somente para retenção com status 01
                    # ///////////////////////////////////////////////////////////////////////////////////////////////////
                    if istatret in (1, 2):
                        sauxi001 = 'SELECT defmeto FROM abnf_operacional_movimentacao_programacao_automacao WHERE situreg != "C" ORDER BY dtmetod DESC LIMIT 1;'
                        lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                        if lsqlre01 == [] or (iqtdre01 > 0 and lsqlre01[0][0] == 'M'):
                            ddataama = abnf_soma_dias_data(date.today(), 1)
                            lcamposb = ('idveicu', None)
                            lfilbusc = (('dataope', '=', ddataama), ('idveicu', '=', iidveicu), ('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
                            lorderby = ('seghini', None)
                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_diario', lcamposb, lfilbusc, lorderby)
                            # Debug (início)
                            # abnf_show('06', lsqlre01, 1)
                            # abnf_show('07', iqtdre01, 0)
                            # Debug (fim)
                            if lsqlre01 != [] and iqtdre01 > 0:
                                bvalidad = False
                                abnf_alert('O veículo selecionado já está alocado no dia de amanhã! É necessário a desalocação deste para poder ser retido com status 01!', 5)
                                abnf_socket_004([5, 'btretvei'])                        
                    if bvalidad:
                        # ///////////////////////////////////////////////
                        # Buscando o GSD (caso ele tenha sido selecionado
                        # ///////////////////////////////////////////////
                        if iidsdede > 0:
                            bvalidad = False
                            lidsdede = abnf_database_sqlx(icodbase, 'X', '12008B', 0, (iidsdede, None))
                            # Debug: (inicio)
                            # abnf_show('10', lidsdede, 0)
                            # Debug: (fim)
                            if lidsdede == []:
                                abnf_alert('Erro interno! Não foi encontrado o registro de GSD ID ' + str(iidsdede) + '! Entre em contato com o depto. de sistemas!', 4)
                                abnf_socket_004([5, 'btretvei'])
                            elif len(lidsdede) != 1:
                                abnf_alert('Erro interno! Mais de um registro de GSD para o ID ' + str(iidsdede) + '! Entre em contato com o depto. de sistemas!', 4)
                                abnf_socket_004([5, 'btretvei'])
                            elif lidsdede[0][0] != iidfilia:
                                abnf_alert('Não é possível concluir esta retenção porque o registro de GSD não pertence a esta filial!', 5)
                                abnf_socket_004([5, 'btretvei'])
                            elif lidsdede[0][1] != 'A':
                                abnf_alert('Não é possível concluir esta retenção porque o grupo do registro de GSD não esta ativo!', 5)
                                abnf_socket_004([5, 'btretvei'])
                            elif lidsdede[0][2] != 'A':
                                abnf_alert('Não é possível concluir esta retenção porque o subgrupo do registro de GSD não esta ativo!', 5)
                                abnf_socket_004([5, 'btretvei'])
                            elif lidsdede[0][3] != 'A':
                                abnf_alert('Não é possível concluir esta retenção porque o registro de GSD não esta ativo!', 5)
                                abnf_socket_004([5, 'btretvei'])
                            else:
                                bvalidad = True
                        if bvalidad:
                            # ////////////////////////////////////////////////////////////////////////
                            # Buscando e analisando o grupo do usuário que esta solicitando a retenção
                            # ////////////////////////////////////////////////////////////////////////
                            lauxi001 = abnf_database_sqlx(icodbase, 'X', '13021A', 0, (iidfilia, iidusuar))
                            if lauxi001 == [] or lauxi001[0][3] != 'A' or lauxi001[0][4] != 'A':
                                abnf_alert('Seu usuário não tem permissão para realizar este procedimento!', 5)
                                abnf_socket_004([5, 'btretvei'])
                            else:
                                iidcusgr = lauxi001[0][0]
                                icodctrl = abnf_database_valor_maximo_campo(icodbase, 'abnf_operacional_movimentacao_programacao_retencao_veiculos', 'codctrl', iidfilia) + 1       
                                # /////////////////////////////////
                                # Salvando nova retenção de veículo
                                # /////////////////////////////////
                                iseghage = abnf_converte_hora_string_em_segundos(hseghage)
                                bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_movimentacao_programacao_retencao_veiculos', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                [
                                    ('codctrl', icodctrl),
                                    ('idveicu', iidveicu),
                                    ('dtreten','CURRENT_TIMESTAMP'),
                                    ('idcusgr', iidcusgr),
                                    ('idcusre', iidusuar),
                                    ('dataage', ddataage),
                                    ('seghage', iseghage),
                                    ('descrre', sdescrre),
                                    ('statret', istatret),
                                    ('idsdede', iidsdede),
                                    ('idfilia', iidfilia),
                                    ('situreg', 'A'),
                                ])
                                if not bvalidad:
                                    abnf_alert('Erro ao criar registros de retenção de veículos! Entre em contato com o depto. de sistemas!', 4)
                                else:
                                    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                    # Buscando e removendo o veículo da programação diária de amanhã se esta for maior ou igual a data do agendamento
                                    # Isso somente para retenção com status 01
                                    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                    if istatret == (1, 2):
                                        ddataama = abnf_soma_dias_data(date.today(), 1)
                                        if ddataama >= ddataage:
                                            lcamposb = ('idoprdi', 'idveicu')
                                            lfilbusc = (('idfilia', '=', iidfilia), ('dataope', '=', ddataama), ('idveicu', '=', iidveicu), ('situreg', '!=', 'C'))
                                            lorderby = ('dataope', 'idveicu', 'dtregcr')
                                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_diario', lcamposb, lfilbusc, lorderby)
                                            if lsqlre01 != [] and iqtdre01 > 0:    # Significa que não foi criando ainda os registros do dia
                                                for lauxi001 in lsqlre01:
                                                    iidoprdi = lauxi001[0]
                                                    # /////////////////////////////////////////
                                                    # Removendo o veículo da programação diária
                                                    # /////////////////////////////////////////
                                                    bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_movimentacao_programacao_diario', iidoprdi, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                                    [
                                                        ('idveicu', None),
                                                    ])
                                                    if not bvalidad:
                                                        abnf_alert('Erro ao remover veículo de registro de diário de programação! Entre em contato com o depto. de sistemas!', 4)
                                                        break
                                    if bvalidad:
                                        abnf_socket_004([10, 'btretvex'])     # Desabilita o botão
                                        abnf_socket_004([10, 'btcancel'])     # Desabilita o botão
                                        scodctrl = str(1000000 + icodctrl)[1:]
                                        abnf_alert('Controle ' + scodctrl +  ': Veículo ' + sprefvei + ' retido com sucesso!', 3)
                                        time.sleep(2)
                                        abnf000u13m02100_operacional_programacao_movimentacao_controle_diario(dabnfopg, True if istatret in (1, 2) else False)
        elif dabnfopg['abnfobj0'] == ['btlibvei', 'btlibvei']:
            # ///////////////
            # Liberar veículo
            # ///////////////
            lmfields = [
                ['sdescrli', 'textarea', 'F', 'descrição adicional de liberação', [], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btretvei')
            if bvalidad:
                iidoprrv = dglobaux['iidoprrv']
                sdescrli = lmfields[0][5]
                lauxi001 = abnf_database_sqlx(icodbase, 'X', '13021A', 0, (iidfilia, iidusuar))
                if lauxi001 == [] or lauxi001[0][3] != 'A' or lauxi001[0][4] != 'A':
                    abnf_alert('Seu usuário não tem permissão para realizar este procedimento!', 5)
                    abnf_socket_004([5, 'btlibvei'])
                else:
                    # ///////////////////////////////////////
                    # Busca o registro de retenção do veículo
                    # ///////////////////////////////////////
                    sauxi001 = 'SELECT '
                    # Campos das tabelas
                    sauxi001 = sauxi001 + 'abnf02.prefvei, '    # [00] Prefixo do veículo
                    sauxi001 = sauxi001 + 'abnf02.placave, '    # [01] Placa do veículo
                    sauxi001 = sauxi001 + 'abnf01.codctrl, '    # [02] Código de controle
                    sauxi001 = sauxi001 + 'abnf01.idcusgr, '    # [03] ID do grupo que reteve
                    sauxi001 = sauxi001 + 'abnf01.situreg, '    # [04] Situação do registro de veículo
                    sauxi001 = sauxi001 + 'abnf01.idfilia, '    # [05] ID da Filial
                    sauxi001 = sauxi001 + 'abnf01.dtliber, '    # [06] Data/hora de liberação
                    sauxi001 = sauxi001 + 'abnf01.statret  '    # [07] Status da retenção
                    # Tabelas SQL
                    sauxi001 = sauxi001 + 'FROM       abnf_operacional_movimentacao_programacao_retencao_veiculos AS abnf01 '
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos                                      AS abnf02 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_grupos_usuarios                   AS abnf03 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idcusgr = abnf03.idcusgr '
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_sistema_usuarios                                       AS abnf04 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idcusre = abnf04.idusuar '
                    # Condições SQL
                    sauxi001 = sauxi001 + 'WHERE '
                    sauxi001 = sauxi001 + 'abnf01.idfilia = ' + str(iidfilia) + ' AND ' # ==> Somente registros da filial
                    sauxi001 = sauxi001 + 'abnf01.situreg != "C" AND '                  # ==> Somente registros não cancelados (retenção)
                    sauxi001 = sauxi001 + 'abnf01.idoprrv = ' + str(iidoprrv) + ';'     # ==> Buscando o registro da retenção
                    # Execução
                    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                    # Debug (início)
                    # abnf_show('05', lsqlre01, 1)
                    # abnf_show('06', lauxi001, 1)
                    # Debug (fim)
                    # ///////////////////////////////////
                    # Abastece a tela de veículos retidos
                    # ///////////////////////////////////
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('Registro de retenção de veículo não encontrado! Entre em contato com o depto. de sistemas!', 4)
                        abnf_socket_004([5, 'btlibvei'])
                    else:
                        sprefvei = lsqlre01[0][0] + ' (' + lsqlre01[0][1] + ')'
                        scodctrl = str(1000000 + lsqlre01[0][2])[1:]
                        iidcusgr = lsqlre01[0][3]
                        ssitureg = lsqlre01[0][4]
                        iidfilix = lsqlre01[0][5]
                        ddtliber = lsqlre01[0][6]
                        istatret = lsqlre01[0][7]
                        if ssitureg != 'A':
                            abnf_alert('Este registro de retenção não pode ser aberto porque não está mais ativo!', 5)
                            abnf_socket_004([5, 'btlibvei'])
                        elif iidfilix != iidfilia:
                            abnf_alert('Este registro de retenção não pode ser aberto porque não pertence a esta filial!', 5)
                            abnf_socket_004([5, 'btlibvei'])
                        elif ddtliber != None:
                            abnf_alert('Este registro de retenção não pode ser aberto porque ja foi liberado!', 5)
                            abnf_socket_004([5, 'btlibvei'])
                        elif iidcusgr != lauxi001[0][0]:
                            abnf_alert('Este registro de retenção não pode ser liberado porque não pertence ao seu grupo de usuário!', 5)
                            abnf_socket_004([5, 'btlibvei'])
                        else:
                            # ////////////////////////////////////////////////////
                            # Liberando o veículo no registros retenção de veículo
                            # ////////////////////////////////////////////////////
                            bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_movimentacao_programacao_retencao_veiculos', iidoprrv, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('dtliber','CURRENT_TIMESTAMP'),
                                ('idcusli', iidusuar),
                                ('descrli', sdescrli),
                            ])
                            if not bvalidad:
                                abnf_alert('Erro ao liberar registro de retenção de veículos! Entre em contato com o depto. de sistemas!', 4)
                            else:
                                abnf_socket_004([10, 'btlibvex'])     # Desabilita o botão
                                abnf_socket_004([10, 'btcancel'])     # Desabilita o botão
                                abnf_alert('Controle ' + scodctrl +  ': Veículo ' + sprefvei + ' liberado com sucesso!', 3)
                                time.sleep(2)
                                abnf000u13m02100_operacional_programacao_movimentacao_controle_diario(dabnfopg, True if istatret in (1, 2) else False)
        elif dabnfopg['abnfobj0'] == ['btgerrel', 'btgerrel']:
            # //////////
            # Relatórios
            # //////////
            abnf_socket_004([5, 'btcancel'])    # Habilita o botão de cancelar
            lmfields = [
                ['irelator', 'select',   'M', 'relatório',              ['Notnull', 'D', 'Return_integer' ], None],
                ['ddataini', 'date',     'F', 'data inicial',           ['Return_date'                    ], None],
                ['hhoraini', 'time-1',   'M', 'horário inicial',        ['Notnull', 'D'                   ], None],
                ['ddatafim', 'date',     'F', 'data final',             ['Return_date'                    ], None],
                ['hhorafim', 'time-1',   'M', 'horário final',          ['Notnull', 'D'                   ], None],
                ['iidveicu', 'select',   'M', 'veículo',                ['Return_integer'                 ], None],
                ['iidsdede', 'select',   'M', 'GSD',                    ['Return_integer'                 ], None],
                ['bstatu01', 'checkbox', 'M', 'status 01',              [                                 ], None],
                ['bstatu02', 'checkbox', 'M', 'status 02',              [                                 ], None],
                ['bstatu03', 'checkbox', 'M', 'status 03',              [                                 ], None],
                ['bstatu04', 'checkbox', 'M', 'status 04',              [                                 ], None],
                ['ddats01i', 'date',     'F', 'data inicial status 01', ['Return_date'                    ], None],
                ['ddats01f', 'date',     'F', 'data final status 01',   ['Return_date'                    ], None],
                ['ddats02i', 'date',     'F', 'data inicial status 01', ['Return_date'                    ], None],
                ['ddats02f', 'date',     'F', 'data final status 01',   ['Return_date'                    ], None],
                ['ddats03i', 'date',     'F', 'data inicial status 01', ['Return_date'                    ], None],
                ['ddats03f', 'date',     'F', 'data final status 01',   ['Return_date'                    ], None],
                ['ddats04i', 'date',     'F', 'data inicial status 01', ['Return_date'                    ], None],
                ['ddats04f', 'date',     'F', 'data final status 01',   ['Return_date'                    ], None],
                ['iformrel', 'select',   'M', 'formato do relatório',   ['Notnull', 'D', 'Return_integer' ], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btgerrel')
            if bvalidad:
                irelator = lmfields[0][5]
                ddataini = lmfields[1][5]
                hhoraini = lmfields[2][5]
                ddatafim = lmfields[3][5]
                hhorafim = lmfields[4][5]
                iidveicu = lmfields[5][5]
                iidsdede = lmfields[6][5]
                bstatu01 = lmfields[7][5]
                bstatu02 = lmfields[8][5]
                bstatu03 = lmfields[9][5]
                bstatu04 = lmfields[10][5]
                ddats01i = lmfields[11][5]
                ddats01f = lmfields[12][5]
                ddats02i = lmfields[13][5]
                ddats02f = lmfields[14][5]
                ddats03i = lmfields[15][5]
                ddats03f = lmfields[16][5]
                ddats04i = lmfields[17][5]
                ddats04f = lmfields[18][5]
                # Debug (início)
                # abnf_show('05', ddats01i, 0)
                # Debug (fim)                
                iformrel = lmfields[19][5]
                ihoraini = abnf_converte_hora_string_em_segundos(hhoraini)
                ihorafim = abnf_converte_hora_string_em_segundos(hhorafim)
                if bvalidad:
                    if ddataini == ddatafim and ihorafim < ihoraini:
                        bvalidad = False
                        abnf_alert('O horário final tem que ser o maior que o inicial!', 5)
                        abnf_socket_004([5, 'btgerrel'])
                if bvalidad:
                    if irelator in (6, 7) and ddataini != ddatafim:
                        bvalidad = False
                        abnf_alert('Para esse relatório, é necessário que as datas inicial e final sejam iguais!', 5)
                        abnf_socket_004([5, 'btgerrel'])
                if bvalidad:
                    if irelator != 11:
                        if ddataini == None:
                            bvalidad = False
                            abnf_alert('A data inicial tem que ser definida!', 5)
                            abnf_socket_004([5, 'btgerrel'])
                        elif ddatafim == None:
                            bvalidad = False
                            abnf_alert('A data final tem que ser definida!', 5)
                            abnf_socket_004([5, 'btgerrel'])
                        else:
                            lmrulesx = [
                                ['e2>=e1', ddataini, 'F', 'data inicial', ddatafim, 'F', 'data final' ],
                            ]
                            bvalidad = abnf_check_rules_fields(lmrulesx, 'btgerrel')
                if bvalidad:
                    if irelator == 11:
                        bvalidad = False
                        if   ddats01i != None and ddats01f != None and ddats01i <= ddats01f: bvalidad = True
                        elif ddats02i != None and ddats02f != None and ddats02i <= ddats02f: bvalidad = True
                        elif ddats03i != None and ddats03f != None and ddats03i <= ddats03f: bvalidad = True
                        elif ddats04i != None and ddats04f != None and ddats04i <= ddats04f: bvalidad = True
                        else: 
                            abnf_alert('Para esse relatório, é necessário ter pelo menos um período das datas de status definida!', 5)
                            abnf_socket_004([5, 'btgerrel'])
                if bvalidad:    
                    abnf000u13m02104_operacional_programacao_movimentacao_controle_diario(dabnfopg, irelator, ddataini, ihoraini, ddatafim, ihorafim,
                    iidveicu, iidsdede, bstatu01, bstatu02, bstatu03, bstatu04, ddats01i, ddats01f, ddats02i, ddats02f, ddats03i, ddats03f, ddats04i, ddats04f, iformrel)
        elif dabnfopg['sonblurx'] == '13M021A':                     # Altera as informações dos campos de data inicial e data final conforme o relatório que foi selecionado
            # ////////////////////////////////////////////////////////////////////////////////////////////
            # Quando selecionar o relatório 12, as datas de inicio de fim são alteradas para o dia de hoje
            # ////////////////////////////////////////////////////////////////////////////////////////////
            lmfields = [
                ['irelator', 'select', 'M', 'relatório', ['Return_integer' ], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btinsitx')
            if bvalidad:
                irelator = lmfields[0][5]
                # ==> if irelator in (11, 12):
                # ==>     sdatahoj = str(date.today())
                # ==>     abnf_socket_004([3, 'ddataini', sdatahoj])
                # ==>    abnf_socket_004([3, 'ddatafim', sdatahoj])
        elif dabnfopg['abnfobj0'] == ['btaltera', 'btaltera']:
            # /////////////////////
            # Alteração de veículos
            # /////////////////////
            lmfields = [
                ['iidoprdi', 'select',   'M', 'registro',    ['Notnull', 'D', 'Return_integer' ], None],
                ['iidveicu', 'select',   'M', 'veículo',     ['Notnull', 'D', 'Return_integer' ], None],
                ['iidomsub', 'select',   'M', 'motivo',      ['Notnull', 'D', 'Return_integer' ], None],
                ['smotisub', 'textarea', 'M', 'complemento', [],                                  None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btaltera')
            if bvalidad:
                iidoprdi = lmfields[0][5]
                iidveicu = lmfields[1][5]
                iidomsub = lmfields[2][5]
                smotisub = lmfields[3][5]
                # //////////////////////////////////////
                # Busca o registro da programação diária
                # //////////////////////////////////////
                # ==> lcamposb = ('idveicu', 'veicger', 'seghini', 'dataope')
                # ==> lfilbusc = (('idoprdi', '=', iidoprdi), ('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
                # ==> lorderby = None
                # ==> lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_diario', lcamposb, lfilbusc, lorderby)
                sauxi001 = 'SELECT '
                # Campos das tabelas
                sauxi001 = sauxi001 + 'abnf02.idveicu, '    # [00] ID do veículo
                sauxi001 = sauxi001 + 'abnf02.veicger, '    # [01] Veículo geral
                sauxi001 = sauxi001 + 'abnf02.seghini, '    # [02] Horário de início (em segundos)
                sauxi001 = sauxi001 + 'abnf02.dataope, '    # [03] Data da operação
                sauxi001 = sauxi001 + 'abnf01.qtporve, '    # [04] Quantidade padrão de portas dos veículos da linha
                sauxi001 = sauxi001 + 'abnf01.perqtpd, '    # [05] Permite veículos com quantidade de portas divergente do padrão
                sauxi001 = sauxi001 + 'abnf01.perveca, '    # [06] Permite veículos com ar-condicionado
                sauxi001 = sauxi001 + 'abnf01.pervesa  '    # [07] Permite veículos sem ar-condicionado
                # ==> sauxi001 = sauxi001 + 'abnf03.prefvei, '    # [08] Prefixo do veículo
                # ==> sauxi001 = sauxi001 + 'abnf03.numport, '    # [09] Número de portas do veículo
                # ==> sauxi001 = sauxi001 + 'abnf03.arcondi  '    # [10] Veículo tem ar-condicionado?
                # Tabelas SQL
                sauxi001 = sauxi001 + 'FROM       abnf_operacional_cadastro_linhas                 AS abnf01 '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_programacao_diario AS abnf02 '
                sauxi001 = sauxi001 + 'ON         abnf01.idolinh = abnf02.idolinh '
                # ==> sauxi001 = sauxi001 + 'LEFT JOIN  abnf_cadastro_veiculos                           AS abnf03 '
                # ==> sauxi001 = sauxi001 + 'ON         abnf02.idveicu = abnf03.idveicu '
                # Condições
                sauxi001 = sauxi001 + 'WHERE abnf02.situreg != "C" '                    # ==> Somente registros não cancelados (diário)
                sauxi001 = sauxi001 + 'AND   abnf02.idoprdi = ' + str(iidoprdi) + ';'   # ==> Somente registros da filial
                # Execução
                lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                if lsqlre01 == [] and iqtdre01 == 0:
                    abnf_alert('Registro de programação não encontrado! Entre em contato com o depto. de sistemas!', 4)
                else:
                    iidveicx = lsqlre01[0][0]
                    iveicger = lsqlre01[0][1]
                    iseghini = lsqlre01[0][2]
                    ddataope = lsqlre01[0][3]
                    iqtporve = lsqlre01[0][4]
                    bperqtpd = lsqlre01[0][5]
                    bperveca = lsqlre01[0][6]
                    bpervesa = lsqlre01[0][7]
                    # Debug (início)
                    # abnf_show('05', lmfields, 1)
                    # abnf_show('06', lsqlre01, 1)
                    # Debug (fim)
                    if iidveicu == iidveicx:
                        abnf_alert('O registro já está com o veículo que foi selecionado!', 5)
                        abnf_socket_004([5, 'btaltera'])
                    elif iidveicu == -1 and iidveicx == None:
                        abnf_alert('O registro já está sem veículo!', 5)
                        abnf_socket_004([5, 'btaltera'])
                    else:
                        # //////////////////////////////////////////////////////////////////
                        # Verifica se o novo veículo é compatível com as exigências da linha
                        # //////////////////////////////////////////////////////////////////
                        if bvalidad:
                            if iidveicu != -1:
                                lcamposb = ('situreg', 'idfilia', 'prefvei', 'numport', 'arcondi')
                                lfilbusc = (('idveicu', '=', iidveicu), ('situreg', '!=', 'C'))
                                lorderby = None
                                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                                if lsqlre01 == [] or iqtdre01 == 0:
                                    bvalidad = False
                                    abnf_alert('Veículo não encontrado! Entre em contato com o depto. de sistemas!', 4)
                                    abnf_socket_004([5, 'btaltera'])
                                elif lsqlre01[0][0] != 'A':
                                    bvalidad = False
                                    abnf_alert('O veículo solicitado não esta ativo!', 5)
                                    abnf_socket_004([5, 'btaltera'])
                                elif lsqlre01[0][1] != iidfilia:
                                    bvalidad = False
                                    abnf_alert('O veículo solicitado não pertence a esta filial!', 5)
                                    abnf_socket_004([5, 'btaltera'])
                                else:
                                    sprefvei = lsqlre01[0][2]
                                    inumport = lsqlre01[0][3]
                                    barcondi = lsqlre01[0][4]
                                    if iqtporve > inumport and bperqtpd == False:      # Quantidade de portas divergente sem permissão de divergência
                                        bvalidad = False
                                        abnf_alert('O veículo ' + sprefvei + ' não tem a quantidade de portas exigidas para esta linha!', 5)
                                        abnf_socket_004([5, 'btaltera'])
                                    elif bperveca == False and barcondi == True:        # Linha não permite com ar-condicionado e veículo possui ar condicionado
                                        bvalidad = False
                                        abnf_alert('O veículo ' + sprefvei + ' possui ar condicionado e isso não é permitido nesta linha!', 5)
                                        abnf_socket_004([5, 'btaltera'])
                                    elif bpervesa == False and barcondi == False:       # Linha não permite sem ar-condicionado e veículo não possui ar condicionado
                                        bvalidad = False
                                        abnf_alert('O veículo ' + sprefvei + ' não possui ar condicionado e isso é exigido nesta linha!', 5)
                                        abnf_socket_004([5, 'btaltera'])
                        # ///////////////////////////////////////////////////////////////////////////////////////////////////////
                        # Verifica se existe algum dos registros posteriores a estes (baseado nos horário) que tenha substituição
                        # Se encontrar não pode permitir que alterações com horário inferior possam ser realizadas
                        # Essa verificação feita baseada no veículo geral
                        # ///////////////////////////////////////////////////////////////////////////////////////////////////////
                        if bvalidad:
                            sauxi001 = 'SELECT '
                            # Campos das tabelas
                            sauxi001 = sauxi001 + 'abnf02.idoprdi '     # [00] ID do registro de diário de programação
                            # Tabelas SQL
                            sauxi001 = sauxi001 + 'FROM       abnf_operacional_movimentacao_programacao_diario       AS abnf01 '
                            sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_programacao_substituicao AS abnf02 '
                            # Condições SQL
                            sauxi001 = sauxi001 + 'WHERE abnf01.idoprdi = abnf02.idoprdi '              # ==> Chave join dos registros
                            # Condições SQL
                            sauxi001 = sauxi001 + 'AND   abnf01.situreg != "C" '                        # ==> Somente registros não cancelados (linhas)
                            sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                        # ==> Somente registros não cancelados (diário)
                            sauxi001 = sauxi001 + 'AND   abnf01.idfilia = ' + str(iidfilia) + ' '       # ==> Somente registros da filial
                            sauxi001 = sauxi001 + 'AND   abnf01.dataope = "' + str(ddataope) + '" '     # ==> Somente registros da data em análise
                            sauxi001 = sauxi001 + 'AND   abnf01.seghini > ' + str(iseghini) + ' '       # ==> Somente registros com horário acima
                            sauxi001 = sauxi001 + 'AND   abnf01.veicger = ' + str(iveicger) + ' '       # ==> Busca pelo veiculo geral
                            # Ordenação
                            sauxi001 = sauxi001 + 'ORDER BY abnf01.seghini DESC LIMIT 1;'               # ==> Pegar somente o ultimo registro do select
                            # Execução
                            lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                            if lsqlre01 != [] and iqtdre01 > 0:
                                bvalidad = False
                                abnf_alert('Não é permitido criar alterações no registro selecionado porque existem alterações posteriores!', 5)
                                abnf_socket_004([5, 'btaltera'])
                        # ////////////////////////////////////////////////////////////////////////////////////////
                        # Verifica se o veículo selecionado não esta sendo usado acima do horário definido
                        # Se encontrar não pode permitir que alterações com horário inferior possam ser realizadas
                        # ////////////////////////////////////////////////////////////////////////////////////////
                        if bvalidad:
                            if iidveicu != None:
                                lcamposb = ('seghini', 'idveicu')
                                lfilbusc = (('dataope', '=', ddataope), ('idveicu', '=', iidveicu), ('seghini', '>', iseghini), ('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
                                lorderby = ('seghini', None)
                                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_diario', lcamposb, lfilbusc, lorderby)
                                # Debug (início)
                                # abnf_show('06', lsqlre01, 1)
                                # abnf_show('07', iqtdre01, 0)
                                # Debug (fim)
                                if lsqlre01 != [] and iqtdre01 > 0:
                                    bvalidad = False
                                    abnf_alert('O veículo selecionado já está sendo usado em horário posterior ao do registro!', 5)
                                    abnf_socket_004([5, 'btaltera'])
                        # ///////////////////////////////////////////////////////////////
                        # Verifica se o veículo selecionado não esta retido com status 01
                        # ///////////////////////////////////////////////////////////////
                        if bvalidad:
                            if iidveicu != None:
                                lcamposb = ('dataage', None)
                                lfilbusc = (('idveicu', '=', iidveicu), ('statret', '=', 1), ('dataage', '<=', ddataope), ('dtliber', '[Null]'), ('situreg', '=', 'A'))
                                lorderby = None
                                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_retencao_veiculos', lcamposb, lfilbusc, lorderby)
                                # Debug (início)
                                # abnf_show('06', lsqlre01, 1)
                                # abnf_show('07', iqtdre01, 0)
                                # Debug (fim)
                                if lsqlre01 != [] and iqtdre01 > 0:
                                    bvalidad = False
                                    abnf_alert('O veículo selecionado esta retido com status 01 na data ' + abnf_converte_data(lsqlre01[0][0]) + '!', 5)
                                    abnf_socket_004([5, 'btaltera'])
                        # ///////////////////////////////////////////////////////////////
                        # Verifica se o veículo selecionado não esta retido com status 02
                        # ///////////////////////////////////////////////////////////////
                        if bvalidad:
                            if iidveicu != None:
                                lcamposb = ('dataage', None)
                                lfilbusc = (('idveicu', '=', iidveicu), ('statret', '=', 2), ('dataage', '<=', ddataope), ('dtliber', '[Null]'), ('situreg', '=', 'A'))
                                lorderby = None
                                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_retencao_veiculos', lcamposb, lfilbusc, lorderby)
                                # Debug (início)
                                # abnf_show('06', lsqlre01, 1)
                                # abnf_show('07', iqtdre01, 0)
                                # Debug (fim)
                                if lsqlre01 != [] and iqtdre01 > 0:
                                    bvalidad = False
                                    abnf_alert('O veículo selecionado esta retido com status 02 na data ' + abnf_converte_data(lsqlre01[0][0]) + '!', 5)
                                    abnf_socket_004([5, 'btaltera'])
                        # /////////////////////////////////////////////
                        # Verifica se o motivo de substituição é valido
                        # /////////////////////////////////////////////
                        if bvalidad:
                            if iidveicu != None:
                                lcamposb = ('situreg', 'idfilia')
                                lfilbusc = (('idomsub', '=', iidomsub), None)
                                lorderby = None
                                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_motivo_substituicao', lcamposb, lfilbusc, lorderby)
                                # Debug (início)
                                # abnf_show('06', lsqlre01, 1)
                                # abnf_show('07', iqtdre01, 0)
                                # Debug (fim)
                                if lsqlre01 == [] or iqtdre01 == 0:
                                    bvalidad = False
                                    abnf_alert('Motivo não encontrado! Entre em contato com o depto. de sistemas!', 4)
                                    abnf_socket_004([5, 'btaltera'])
                                elif lsqlre01[0][0] != 'A':
                                    bvalidad = False
                                    abnf_alert('O motivo selecionado não esta ativo!', 5)
                                    abnf_socket_004([5, 'btaltera'])
                                elif lsqlre01[0][1] != iidfilia:
                                    bvalidad = False
                                    abnf_alert('O motivo selecionado não pertence a esta filial!', 5)
                                    abnf_socket_004([5, 'btaltera'])
                        # /////////////////////////////////////
                        # Cria um novo registro de substituição
                        # /////////////////////////////////////
                        if bvalidad:
                            iidveien = iidveicu if iidveicu != -1 else None
                            validad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_movimentacao_programacao_substituicao', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('idoprdi', iidoprdi),
                                ('tiposub', 'V'),
                                ('idveisa', iidveicx),
                                ('idveien', iidveien),
                                ('idomsub', iidomsub),
                                ('motisub', smotisub),
                                ('idfilia', iidfilia),
                                ('situreg', 'A'),
                            ])
                            if not bvalidad:
                                abnf_alert('Erro ao criar registros da substituição! Entre em contato com o depto. de sistemas!', 4)
                        # //////////////////////////////////////////////////////
                        # Atualiza todos o registros que envolvem a ação tomada
                        # Duas ações diferentes aqui pode aconteder
                        # //////////////////////////////////////////////////////
                        if bvalidad:
                            # /////////////////////////////////
                            # Desabilita os dois botões do form
                            # /////////////////////////////////
                            abnf_socket_004([10, sauxi001])
                            abnf_socket_004([10, sauxi001])
                            # ///////////////////////////////////////////////////////////////////////////////////
                            # Ação 01: Foi somente removido o veículo e deixado sem nenhum (iidveicu == -1)
                            # 01.a) Buscar todos os veículos na data do registro selecionado (ddataope)
                            # 01.b) Filtrar somente os horários maior ou igual ao registro selecionado (iseghini)
                            # Ação 02: Foi alterado o veículo atual por outro veículo (iidveicu != -1) 
                            # 02.a) Buscar todos os veículos gerais na data do registro selecionado (ddataope)
                            # 02.b) Filtrar somente os horários maior ou igual ao registro selecionado (iseghini)
                            # ///////////////////////////////////////////////////////////////////////////////////
                            sauxi001 = 'UPDATE abnf_operacional_movimentacao_programacao_diario SET '
                            if iidveicu == -1:  sauxi001 = sauxi001 + 'idveicu = NULL '                         # ==> Remove os veículos dos registros
                            else:               sauxi001 = sauxi001 + 'idveicu = ' + str(iidveicu) + ' '        # ==> Altera os veículos dos registros
                            if iidveicu == -1:  sauxi001 = sauxi001 + 'WHERE idveicu = ' + str(iidveicx) + ' '  # ==> Busca pelo veiculo registrado
                            else:               sauxi001 = sauxi001 + 'WHERE veicger = ' + str(iveicger) + ' '  # ==> Busca pelo veiculo geral
                            sauxi001 = sauxi001 + 'AND   situreg != "C" '                                       # ==> Somente registros não cancelados
                            sauxi001 = sauxi001 + 'AND   idfilia = ' + str(iidfilia) + ' '                      # ==> Somente registros da filial
                            sauxi001 = sauxi001 + 'AND   dataope = "' + str(ddataope) + '" '                    # ==> Somente registros da data em análise
                            sauxi001 = sauxi001 + 'AND   seghini >= ' + str(iseghini) + ';'                     # ==> Somente registros com horário acima
                            # Debug (início)
                            # abnf_show('06', sauxi001, 0)
                            # abnf_show('07', iidveicu, 0)
                            # Debug (fim)
                            bvalidad = abnf_database_executa_sql_commit(icodbase, sabnproj, sauxi001, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                            if not bvalidad:
                                abnf_alert('Erro ao remover veículo de registros de programação diária! Entre em contato com o depto. de sistemas!', 4)
                            else:
                                if iidveicu != -1 and iqtporve > inumport:
                                    sauxi001 = 'Alteração realizada com sucesso! No entanto, o veículo está com quantidade de portas fora do padrão da linha, por isso, deve ser substituído assim que possível!'
                                else:
                                    sauxi001 = 'Alteração realizada com sucesso!'
                                abnf_alert(sauxi001, 3)
                                time.sleep(3)
                                abnf000u13m02100_operacional_programacao_movimentacao_controle_diario(dabnfopg)     # Voltar para tela principal
                                # abnf_socket_004([3, 'iidoprdi', ''])        # Limpa o campo
                                # abnf_socket_004([3, 'iidveicu', ''])        # Limpa o campo
                                # abnf_socket_004([3, 'iidomsub', ''])        # Limpa o campo
                                # abnf_socket_004([3, 'smotisub', ''])        # Limpa o campo
                                
                                
        elif dabnfopg['abnfobj0'] == ['btcanalt', 'btcanalt']:
            # //////////////////////////
            # Cancelamento de alterações
            # //////////////////////////
            lmfields = [
                ['iidoprsu', 'input', 'M', 'registro de retenção',             ['Notnull', 'D', 'Return_integer' ], None],
                ['ssenhpro', 'input', 'F', 'senha para liberação do processo', ['Notnull', 'P'],                    None], 
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btcanalt')
            if bvalidad:
                iidoprsu = lmfields[0][5]
                ssenhpro = lmfields[1][5]
                if ssenhpro != 'J8X2Q7L0':  # *** Senha ***
                    abnf_alert('Senha inválida!', 4)
                    abnf_socket_004([5, 'btcanalt'])
                else:
                    # ///////////////////
                    # Buscando o registro
                    # ///////////////////
                    lcamposb = ('situreg', 'idfilia')
                    lfilbusc = (('idoprsu', '=', iidoprsu), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_substituicao', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('Registros não encontrado! Verifique se a numeração digitada esta correta!', 4)
                        abnf_socket_004([5, 'btcanalt'])
                    elif lsqlre01[0][0] != 'A':
                        abnf_alert('O registro solicitado não esta ativo!', 5)
                        abnf_socket_004([5, 'btcanalt'])
                    elif lsqlre01[0][1] != iidfilia:
                        abnf_alert('O registro solicitado não pertence a esta filial!', 5)
                        abnf_socket_004([5, 'btcanalt'])
                    else:
                        # //////////////////////////////////
                        # Cancelando o registro de alteração
                        # //////////////////////////////////
                        bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_movimentacao_programacao_substituicao', iidoprsu, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('situreg', 'C'),
                        ])
                        if not bvalidad:
                            abnf_alert('Não foi possível cancelar o registro solicitado! Entre em contato com o depto. de sistemas!', 4)
                            abnf_socket_004([5, 'btcanalt'])
                        else:
                            abnf_socket_004([10, 'btcanalx'])     # Desabilita o botão
                            abnf_socket_004([10, 'btcancel'])     # Desabilita o botão
                            abnf_alert('Registro cancelado com sucesso!', 3)
                            time.sleep(2)
                            abnf000u13m02100_operacional_programacao_movimentacao_controle_diario(dabnfopg, False)
        # ////////////////////////////////
        # Habilita todos os botões do form
        # ////////////////////////////////
        for sauxi001 in lbuttfor:
            abnf_socket_004([5, sauxi001])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13m02103_operacional_programacao_movimentacao_controle_diario ] //////////////////////////////////////////////////////////////////////////// #
# // Programação - Controle Diário.                                                                                                                      // #
# // Cria os registros do dia seguinte e monta as listas de linhas-serviços, de veículos retidos e também atualiza divs de informações.                  // #                                                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13m02103_operacional_programacao_movimentacao_controle_diario(icodbase, sabnproj, dglobaux, iidfilia, balocvei):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13m02103_operacional_programacao_movimentacao_controle_diario(...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # //////////////////////////////////////////////////////////////
    # Entra em modo de espera enquanto existir o arquivo de bloqueio
    # //////////////////////////////////////////////////////////////
    sarqdown = "abnftmp/abnf000u13m02100.now"
    bvalidad = True
    while os.path.isfile(sarqdown):
        if bvalidad:
            abnf_alert('Aguarde! Atualizando informações...', 5)
            bvalidad = False
        time.sleep(1)
    # /////////////////////////////////////
    # Cria o arquivo temporário de bloqueio
    # /////////////////////////////////////
    with open(sarqdown, 'w') as sarquwri:
        sarquwri.write('Atualizando registros de diário de programação...' + '\n')
        sarquwri.write(str(dglobaux['slogiusu']) + '\n')
    # /////////////////////////////////
    # Desabilita todos os botão do form
    # /////////////////////////////////
    lbuttfor = ['btatuinx', 'btrelatx', 'btdesesx', 'btcandia', 'btalthoj', 'btaltama', 'btaltesp', 'btcanalt', 'btatuiny', 'btrelaty', 'btretvei', 'btlibvei']
    for sauxi001 in lbuttfor:
        abnf_socket_004([10, sauxi001])     # Desabilita o botão
    abnf_alert('Aguarde! Atualizando informações...', 15)
    # ///////////////////////////////////
    # Definição de "ddatahoj" e "dataama"
    # ///////////////////////////////////   
    ddatahoj = date.today()
    # ddatahoj = date(2025, 9, 8)   # <= Gerar registro de data específica
    ddataama = abnf_soma_dias_data(ddatahoj, 1)
    ldataaux = [ddatahoj, ddataama]
    ldatager = []
    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    # Verifica se ja foram criados registros do dia de hoje e de de amanhã na tabela de programação diária 
    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    for ddataaux in ldataaux:
        lcamposb = ('dataope', None)
        lfilbusc = (('idfilia', '=', iidfilia), ('dataope', '=', ddataaux), ('situreg', '!=', 'C'))
        lorderby = ('dataope', 'idolinh', 'veicpro')
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_diario', lcamposb, lfilbusc, lorderby)
        if lsqlre01 == [] and iqtdre01 == 0:    # Significa que não foi criando ainda os registros do dia
            ldatager.append(ddataaux)
    # //////////////////////////////////////////////
    # Gera registros na tabela de programação diária
    # //////////////////////////////////////////////
    # if True:
    if ldatager != []:
        balocvei = True # ==> Realiza a alocação de veículos após a criação dos registros
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # Liberação automática de registros de retenções de veículos com status 2, 3 e 4 que tiverem data de agendamento menor que data de hoje
        # A cada primeiro acesso do dia o sistema tem que realizar este procedimento o qual tem que se limitar a apenas uma vez ao dia
        # Para saber se o procedimento ja foi feito no dia, o sistema vai procurar registros na tabela "abnf_operacional_movimentacao_programacao_automacao"
        # Caso encontre qualquer registro ativo com a data maior ou igual de hoje então ele não realiza o procedimento
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        lcamposb = ('dtmetod', None)
        lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C'), ('dtmetod', '>=', ddatahoj))
        lorderby = ('dtmetod', None)
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_automacao', lcamposb, lfilbusc, lorderby)
        if lsqlre01 == [] and iqtdre01 == 0:
            # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            # Os registros de retenções que serão liberados são todos com com status 2, 3 e 4 e que tiverem data de agendamento menor que data de hoje
            # O usuário de liberação (idcusli) será 0 (zero) para indicar ao sistema que o fechamento foi realizado de forma automática
            # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            sauxi001 = 'UPDATE abnf_operacional_movimentacao_programacao_retencao_veiculos SET '
            sauxi001 = sauxi001 + 'dtliber = "' + abnf_websocket_date_time(6) + '", '
            sauxi001 = sauxi001 + 'idcusli = 0, '
            sauxi001 = sauxi001 + 'idusual = ' + str(dglobaux['iidusuar']) + ', '
            sauxi001 = sauxi001 + 'dtregal = CURRENT_TIMESTAMP() '
            sauxi001 = sauxi001 + 'WHERE dataage < "' + str(ddatahoj) + '" and dtliber IS NULL and situreg != "C" and statret IN (2, 3, 4);'
            bvalidad = abnf_database_executa_sql_commit(icodbase, sabnproj, sauxi001, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if not bvalidad:
                abnf_alert('Erro ao rfechar registros de retenções! Entre em contato com o depto. de sistemas!', 4)
        if bvalidad:
            # /////////////////////////////////////
            # Geração de registros da tabela diária
            # /////////////////////////////////////
            for ddataaux in ldatager:
                # ////////////////////////////////////////
                # Definição dos tipos de dias ("dtipodia")
                # ////////////////////////////////////////
                dtipodia = {}
                lcamposb = ('idolinh', 'veicser', 'tipodia', 'descmot')
                lfilbusc = (('idfilia', '=', iidfilia), ('dataope', '=', ddataaux), ('situreg', '!=', 'C'))
                lorderby = ('dataope', 'idolinh', 'veicser', 'idooesp')
                lsqlre02, iqtdre02 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_operacoes_especiais', lcamposb, lfilbusc, lorderby)
                for lauxi001 in lsqlre02:
                    dtipodia[(lauxi001[0], lauxi001[1])] = ((lauxi001[2]), lauxi001[3])
                if dtipodia.get((0, 0), None) == None:
                    dtipodia[(0, 0)] = (abnf_converte_data_semana(ddataaux)[2], None)
                # Debug (início)
                # abnf_show('05', ddataaux, 0)
                # abnf_show('06', dtipodia, 2)
                # Debug (fim)
                # ////////////////////////////////////////////////////////////////////////////////
                # Criando os registros de diário de programação
                # Definição das viagens a serem feitas através da tabela de propostas
                # Futuramente analisar através das OSOs assim que elas estiverem em dia no sistema
                # ////////////////////////////////////////////////////////////////////////////////
                abnf_alert('Aguarde! Gerando registros de diário de programação para a data ' + abnf_converte_data(ddataaux) + '...', 15)
                sauxi001 = 'SELECT '
                # Campos das tabelas
                sauxi001 = sauxi001 + 'abnf01.idolinh, '    # [00] ID da linha
                sauxi001 = sauxi001 + 'abnf01.codolin, '    # [01] Código da linha 
                sauxi001 = sauxi001 + 'abnf01.desolin, '    # [02] Descrição da linha
                sauxi001 = sauxi001 + 'abnf03.veicpro, '    # [03] Veículo da proposta
                sauxi001 = sauxi001 + 'abnf03.veicger, '    # [04] Veículo geral
                sauxi001 = sauxi001 + 'abnf03.sentido, '    # [05] Sentido: [I]da/[V]olta
                sauxi001 = sauxi001 + 'abnf03.tipopon, '    # [06] Tipo de ponto: [O]ficial/[P]assagem/[I]ntermediário
                sauxi001 = sauxi001 + 'abnf03.idotivi, '    # [07] Tipo de viagem: 1=Ocioso/2=Produtivo/3=Reservado/4=Deslocamento 
                sauxi001 = sauxi001 + 'abnf03.seghini, '    # [08] Horário de início (em segundos)
                sauxi001 = sauxi001 + 'abnf03.seghfim, '    # [09] Horário de término (em segundos)
                sauxi001 = sauxi001 + 'abnf04.saidgar, '    # [10] Saída da garagem?
                sauxi001 = sauxi001 + 'abnf03.seghgar, '    # [11] Horário de saída da garagem (em segundos)
                sauxi001 = sauxi001 + 'abnf03.idolori, '    # [12] ID do local de origem (FK)
                sauxi001 = sauxi001 + 'abnf04.codoloc, '    # [13] Código do local de origem
                sauxi001 = sauxi001 + 'abnf04.desoloc, '    # [14] Descrição do local de origem
                sauxi001 = sauxi001 + 'abnf03.idoldes, '    # [15] ID do local de destino (FK)
                sauxi001 = sauxi001 + 'abnf05.codoloc, '    # [16] Código do local de destino
                sauxi001 = sauxi001 + 'abnf05.desoloc, '    # [17] Descrição do local de destino
                sauxi001 = sauxi001 + 'abnf02.tpdiaut, '    # [18] Tipo de dia: U
                sauxi001 = sauxi001 + 'abnf02.tpdiasa, '    # [19] Tipo de dia: S
                sauxi001 = sauxi001 + 'abnf02.tpdiado, '    # [20] Tipo de dia: D
                sauxi001 = sauxi001 + 'abnf02.tpdiafe, '    # [21] Tipo de dia: F
                sauxi001 = sauxi001 + 'abnf02.tpdia2a, '    # [22] Tipo de dia: 2
                sauxi001 = sauxi001 + 'abnf02.tpdia3a, '    # [23] Tipo de dia: 3
                sauxi001 = sauxi001 + 'abnf02.tpdia4a, '    # [24] Tipo de dia: 4
                sauxi001 = sauxi001 + 'abnf02.tpdia5a, '    # [25] Tipo de dia: 5
                sauxi001 = sauxi001 + 'abnf02.tpdia6a  '    # [26] Tipo de dia: 6
                # Tabelas SQL
                sauxi001 = sauxi001 + 'FROM       abnf_operacional_cadastro_linhas                    AS abnf01 '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_propostas_oso         AS abnf02 '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_propostas_oso_viagens AS abnf03 '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_locais                    AS abnf04 '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_locais                    AS abnf05 '
                # Condições SQL
                sauxi001 = sauxi001 + 'WHERE abnf01.idolinh = abnf02.idolinh '                          # ==> Chave join dos registros
                sauxi001 = sauxi001 + 'AND   abnf02.idoprop = abnf03.idoprop '                          # ==> Chave join dos registros
                sauxi001 = sauxi001 + 'AND   abnf03.idolori = abnf04.idoloca '                          # ==> Chave join dos registros
                sauxi001 = sauxi001 + 'AND   abnf03.idoldes = abnf05.idoloca '                          # ==> Chave join dos registros
                # Condições SQL
                sauxi001 = sauxi001 + 'AND   abnf01.situreg = "A" '                                     # ==> Somente registros ativos (linhas)
                sauxi001 = sauxi001 + 'AND   abnf02.situreg = "A" '                                     # ==> Somente registros ativos (proposta)
                sauxi001 = sauxi001 + 'AND   abnf03.situreg != "C" '                                    # ==> Somente registros não cancelados (viagens)
                sauxi001 = sauxi001 + 'AND   abnf04.situreg != "C" '                                    # ==> Somente registros não cancelados (locais)
                # sauxi001 = sauxi001 + 'AND   (abnf04.saidgar = TRUE or abnf03.seghgar IS NOT NULL) '  # ==> Somente locais que forem saída de garagem ou registros de viagens com definição de saida extra da garagem
                # sauxi001 = sauxi001 + 'AND   abnf03.seghgar IS NOT NULL '                             # ==> Somente locais que registros de viagens com definição de saida extra da garagem
                sauxi001 = sauxi001 + 'AND   abnf02.idfilia = ' + str(iidfilia) + ' '                   # ==> Somente registros da filial
                # Ordenação
                sauxi001 = sauxi001 + 'ORDER BY abnf01.codolin, abnf03.veicpro, abnf03.seghini, '
                sauxi001 = sauxi001 + 'abnf02.tpdiaut, '    # Tipo de dia: U
                sauxi001 = sauxi001 + 'abnf02.tpdiasa, '    # Tipo de dia: S
                sauxi001 = sauxi001 + 'abnf02.tpdiado, '    # Tipo de dia: D
                sauxi001 = sauxi001 + 'abnf02.tpdiafe, '    # Tipo de dia: F
                sauxi001 = sauxi001 + 'abnf02.tpdia2a, '    # Tipo de dia: 2
                sauxi001 = sauxi001 + 'abnf02.tpdia3a, '    # Tipo de dia: 3
                sauxi001 = sauxi001 + 'abnf02.tpdia4a, '    # Tipo de dia: 4
                sauxi001 = sauxi001 + 'abnf02.tpdia5a, '    # Tipo de dia: 5
                sauxi001 = sauxi001 + 'abnf02.tpdia6a; '    # Tipo de dia: 6
                lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                # Debug (início)
                # abnf_show('10', sauxi001, 0)
                # Debug (fim)
                # Execução
                # ///////////////////////////////////////////////////////////////////////////////////////////////////
                # Etapa 01 de criação dos registros diários:
                # Guardar em "lauxidia" os dados para criar os registros da programação diária para a data "ddataaux"
                # Para isso tem que ser feito um comparativo em cada registro de viagem com o dicionário "dtipodia"
                # ///////////////////////////////////////////////////////////////////////////////////////////////////
                lauxidia = []
                for lauxi001 in lsqlre01:
                    iidolinh = lauxi001[0]
                    icodolin = lauxi001[1]
                    sdesolin = lauxi001[2]
                    iveicpro = lauxi001[3]
                    iveicger = lauxi001[4]
                    ssentido = lauxi001[5]
                    stipopon = lauxi001[6]
                    iidotivi = lauxi001[7]
                    iseghini = lauxi001[8]
                    iseghfim = lauxi001[9]
                    bsaidgar = lauxi001[10]
                    iseghgar = lauxi001[11]
                    iidolori = lauxi001[12]
                    icodolor = lauxi001[13]
                    sdesolor = lauxi001[14]
                    iidoldes = lauxi001[15]
                    icodolde = lauxi001[16]
                    sdesolde = lauxi001[17]
                    btpdiaut = lauxi001[18]
                    btpdiasa = lauxi001[19]
                    btpdiado = lauxi001[20]
                    btpdiafe = lauxi001[21]
                    btpdia2a = lauxi001[22]
                    btpdia3a = lauxi001[23]
                    btpdia4a = lauxi001[24]
                    btpdia5a = lauxi001[25]
                    btpdia6a = lauxi001[26]
                    if bsaidgar and iseghgar == None:               # Se esta marcado como saida da garagem e iseghgar (horário de saida da garagem) estiver como nulo
                        iseghgar = iseghini                         # iseghgar (horário de saida da garagem) assume o valor do horário de início
                    elif not bsaidgar and iseghgar != None:         # Se não esta marcado como saida da garagem e iseghgar (horário de saida da garagem) estiver definido
                        bsaidgar = True                             # Passa a ser marcado como saída de garagem
                    ltipodia = dtipodia.get((iidolinh, iveicpro), None)
                    if ltipodia == None:
                        ltipodia = dtipodia.get((iidolinh, 0), None)
                        if ltipodia == None:
                            ltipodia = dtipodia.get((0, 0), None)
                    sauxi001 = ''
                    sauxi002 = ''
                    for stipodia in ltipodia[0]:
                        if   stipodia == 'U' and btpdiaut: sauxi001 = sauxi001 + stipodia ; sauxi002 = ltipodia[1] ; break
                        elif stipodia == 'S' and btpdiasa: sauxi001 = sauxi001 + stipodia ; sauxi002 = ltipodia[1] ; break
                        elif stipodia == 'D' and btpdiado: sauxi001 = sauxi001 + stipodia ; sauxi002 = ltipodia[1] ; break
                        elif stipodia == 'F' and btpdiafe: sauxi001 = sauxi001 + stipodia ; sauxi002 = ltipodia[1] ; break
                        elif stipodia == '2' and btpdia2a: sauxi001 = sauxi001 + stipodia ; sauxi002 = ltipodia[1] ; break
                        elif stipodia == '3' and btpdia3a: sauxi001 = sauxi001 + stipodia ; sauxi002 = ltipodia[1] ; break
                        elif stipodia == '4' and btpdia4a: sauxi001 = sauxi001 + stipodia ; sauxi002 = ltipodia[1] ; break
                        elif stipodia == '5' and btpdia5a: sauxi001 = sauxi001 + stipodia ; sauxi002 = ltipodia[1] ; break
                        elif stipodia == '6' and btpdia6a: sauxi001 = sauxi001 + stipodia ; sauxi002 = ltipodia[1] ; break
                    if sauxi001 != '':
                        lauxidia.append([
                            iidolinh, # [00]
                            icodolin, # [01]
                            sdesolin, # [02]
                            iveicpro, # [03]
                            iveicger, # [04]
                            sauxi001, # [05]
                            sauxi002, # [06]
                            ssentido, # [07]
                            stipopon, # [08]
                            iidotivi, # [09]
                            iseghini, # [10]
                            iseghfim, # [11]
                            bsaidgar, # [12]
                            iseghgar, # [13]
                            iidolori, # [14]
                            icodolor, # [15]
                            sdesolor, # [16]
                            iidoldes, # [17]
                            icodolde, # [18]
                            sdesolde, # [19]
                        ])
                # Debug (início)
                # abnf_show('09', lsqlre01, 1)
                # abnf_show('10', lauxidia, 1)
                # Debug (fim)   
                if lauxidia == []:
                    abnf_alert('Nenhum registro de diário de programação foi criado!', 5)
                    bvalidad = False
                    break
                else:
                    # (no novo processo não será necessário essas etapas) # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    # (no novo processo não será necessário essas etapas) # Etapa 02 de criação dos registros diários:
                    # (no novo processo não será necessário essas etapas) # Pegar o primeiro registro produtivo da linha-serviço que tiver o horário igual ou acima do horário de saída de "lauxidia"
                    # (no novo processo não será necessário essas etapas) # Encontrando o registro, pegar o sentido da viagem e gravar em "lauxidia"
                    # (no novo processo não será necessário essas etapas) # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    # (no novo processo não será necessário essas etapas) sauxi001 = 'SELECT '
                    # (no novo processo não será necessário essas etapas) # Campos das tabelas
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf01.idolinh, '    # [00] ID da linha
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf03.veicpro, '    # [01] Veículo-Serviço
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdiaut, '    # [02] Tipo de dia: U
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdiasa, '    # [03] Tipo de dia: S
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdiado, '    # [04] Tipo de dia: D
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdiafe, '    # [05] Tipo de dia: F
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia2a, '    # [06] Tipo de dia: 2
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia3a, '    # [07] Tipo de dia: 3
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia4a, '    # [08] Tipo de dia: 4
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia5a, '    # [09] Tipo de dia: 5
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia6a, '    # [10] Tipo de dia: 6
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf03.seghini, '    # [11] Horário de início (em segundos)
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf03.sentido, '    # [12] Sentido da viagem
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf03.idolori, '    # [13] ID do local de origem
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf04.codoloc, '    # [14] Código do local de origem
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf04.desoloc  '    # [15] Descrição do local de origem
                    # (no novo processo não será necessário essas etapas) # Tabelas SQL
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'FROM       abnf_operacional_cadastro_linhas                    AS abnf01 '
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_propostas_oso         AS abnf02 '
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_propostas_oso_viagens AS abnf03 '
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_locais                    AS abnf04 '
                    # (no novo processo não será necessário essas etapas) # Condições SQL
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'WHERE abnf01.idolinh = abnf02.idolinh '          # ==> Chave join dos registros
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'AND   abnf02.idoprop = abnf03.idoprop '          # ==> Chave join dos registros
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'AND   abnf03.idolori = abnf04.idoloca '          # ==> Chave join dos registros
                    # (no novo processo não será necessário essas etapas) # Condições SQL
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'AND   abnf01.situreg != "C" '                    # ==> Somente registros não cancelados (linhas)
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                    # ==> Somente registros não cancelados (proposta)
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'AND   abnf03.situreg != "C" '                    # ==> Somente registros não cancelados (viagens)
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'AND   abnf04.situreg != "C" '                    # ==> Somente registros não cancelados (locais)
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'AND   idotivi = 2 '                              # ==> Somente viagens produtivas
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'AND   abnf02.idfilia = ' + str(iidfilia) + ' '   # ==> Somente registros da filial
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'ORDER BY abnf01.idolinh, abnf03.veicpro, abnf03.seghini, '
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdiaut, '    # Tipo de dia: U
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdiasa, '    # Tipo de dia: S
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdiado, '    # Tipo de dia: D
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdiafe, '    # Tipo de dia: F
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia2a, '    # Tipo de dia: 2
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia3a, '    # Tipo de dia: 3
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia4a, '    # Tipo de dia: 4
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia5a, '    # Tipo de dia: 5
                    # (no novo processo não será necessário essas etapas) sauxi001 = sauxi001 + 'abnf02.tpdia6a; '    # Tipo de dia: 6
                    # (no novo processo não será necessário essas etapas) lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                    # (no novo processo não será necessário essas etapas) if lsqlre01 != [] and iqtdre01 > 0:
                    # (no novo processo não será necessário essas etapas)     for lauxi001 in lauxidia:
                    # (no novo processo não será necessário essas etapas)         for lauxi002 in lsqlre01:
                    # (no novo processo não será necessário essas etapas)             if lauxi001[1] == lauxi002[0]:                          # Mesma linha
                    # (no novo processo não será necessário essas etapas)                 if lauxi001[2] == lauxi002[1]:                      # Mesmo veículo-serviço
                    # (no novo processo não será necessário essas etapas)                     sauxi001 = ''
                    # (no novo processo não será necessário essas etapas)                     if lauxi002[2]:  sauxi001 = sauxi001 + 'U'
                    # (no novo processo não será necessário essas etapas)                     if lauxi002[3]:  sauxi001 = sauxi001 + 'S'
                    # (no novo processo não será necessário essas etapas)                     if lauxi002[4]:  sauxi001 = sauxi001 + 'D'
                    # (no novo processo não será necessário essas etapas)                     if lauxi002[5]:  sauxi001 = sauxi001 + 'F'
                    # (no novo processo não será necessário essas etapas)                     if lauxi002[6]:  sauxi001 = sauxi001 + '2'
                    # (no novo processo não será necessário essas etapas)                     if lauxi002[7]:  sauxi001 = sauxi001 + '3'
                    # (no novo processo não será necessário essas etapas)                     if lauxi002[8]:  sauxi001 = sauxi001 + '4'
                    # (no novo processo não será necessário essas etapas)                     if lauxi002[9]:  sauxi001 = sauxi001 + '5'
                    # (no novo processo não será necessário essas etapas)                     if lauxi002[10]: sauxi001 = sauxi001 + '6'                                
                    # (no novo processo não será necessário essas etapas)                     if lauxi001[8] in sauxi001:                     # Se o tipo de dia esta incluído no registro
                    # (no novo processo não será necessário essas etapas)                         if lauxi002[11] >= lauxi001[3]:
                    # (no novo processo não será necessário essas etapas)                             lauxi001[4] = lauxi002[12]              # Guarda o sentido
                    # (no novo processo não será necessário essas etapas)                             lauxi001[5] = lauxi002[13]              # Guarda o ID do local de origem
                    # (no novo processo não será necessário essas etapas)                             lauxi001[6] = lauxi002[14]              # Guarda o código do local de origem
                    # (no novo processo não será necessário essas etapas)                             lauxi001[7] = lauxi002[15]              # Guarda a descrição do local de origem
                    # (no novo processo não será necessário essas etapas)                             break
                    # (no novo processo não será necessário essas etapas) # Debug (início)
                    # (no novo processo não será necessário essas etapas) # abnf_show('05', lauxidia, 1)
                    # (no novo processo não será necessário essas etapas) # abnf_show('06', lsqlre01, 1)
                    # (no novo processo não será necessário essas etapas) # Debug (fim)
                    # (no novo processo não será necessário essas etapas) bvalidad = True
                    # (no novo processo não será necessário essas etapas) # //////////////////////////////////////////
                    # (no novo processo não será necessário essas etapas) # Etapa 03 de criação dos registros diários:
                    # (no novo processo não será necessário essas etapas) # Verifica a integridade de "lauxidia"
                    # (no novo processo não será necessário essas etapas) # //////////////////////////////////////////
                    # (no novo processo não será necessário essas etapas) for lauxi001 in lauxidia:
                    # (no novo processo não será necessário essas etapas)     if lauxi001[4] == 'X':
                    # (no novo processo não será necessário essas etapas)         bvalidad = False
                    # (no novo processo não será necessário essas etapas)         sdesolin = abnf_database_find(icodbase, None, '013A', lauxi001[1], None)
                    # (no novo processo não será necessário essas etapas)         abnf_alert('Não foi possível definir a primeira viagem produtiva da linha: ' + sdesolin + ' - serviço: ' + str(lauxi001[2]) + ' - tipo de dia: ' + str(lauxi001[8]), 5)
                    # //////////////////////////////////////////
                    # Etapa 02 de criação dos registros diários:
                    # Geração dos registros na tabela
                    # //////////////////////////////////////////
                    icontd01 = 0
                    for lauxi001 in lauxidia:    
                        validad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_movimentacao_programacao_diario', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('dataope', ddataaux),
                            ('tiporeg', 'A'),
                            ('idolinh', lauxi001[0]),
                            ('codolin', lauxi001[1]),
                            ('desolin', lauxi001[2]),
                            ('veicpro', lauxi001[3]),
                            ('veicger', lauxi001[4]),
                            ('tipodia', lauxi001[5]),
                            ('descmot', lauxi001[6]),
                            ('sentido', lauxi001[7]),
                            ('tipopon', lauxi001[8]),
                            ('idotivi', lauxi001[9]),
                            ('seghini', lauxi001[10]),
                            ('seghfim', lauxi001[11]),
                            ('saidgar', lauxi001[12]),
                            ('seghgar', lauxi001[13]),
                            ('idolori', lauxi001[14]),
                            ('codolor', lauxi001[15]),
                            ('desolor', lauxi001[16]),
                            ('idoldes', lauxi001[17]),
                            ('codolde', lauxi001[18]),
                            ('desolde', lauxi001[19]),
                            ('idfilia', iidfilia),
                            ('situreg', 'A'),
                        ])
                        if not bvalidad:
                            abnf_alert('Erro ao criar registros da programação diária! Entre em contato com o depto. de sistemas!', 4)
                            break
                        else:
                            icontd01 += 1
                    if bvalidad:        
                        if icontd01 == 0:
                            abnf_alert('Nenhum registro de diário de programação foi criado!', 5)
                            bvalidad = False
                            break
                        else:
                            abnf_alert(str(icontd01) + ' registro(s) de diário de programação gerado(s) com sucesso para o dia ' + abnf_converte_data(ddataaux) + ' !', 3)
                            time.sleep(3)
                            abnf_alert('Aguarde! Liberando o robô de alocação automática de veículos...', 5)
                            # //////////////////////////////////////////////////////////////////////////////
                            # Gera um registro de automação que libera o sistema para operar automaticamente
                            # //////////////////////////////////////////////////////////////////////////////
                            bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_movimentacao_programacao_automacao', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('dtmetod', 'CURRENT_TIMESTAMP'),
                                ('defmeto', 'A'),
                                ('idfilia', iidfilia),
                                ('situreg', 'A'),
                            ])
                            if not bvalidad:
                                abnf_alert('Erro ao criar registros de automação de programação! Entre em contato com o depto. de sistemas!', 4)
                                break
    # /////////////////////////////////////////////////////////////////////////////////////////
    # Alocação de veículos nos registros de programação diária.
    # Este processo consiste em remover os veículos atuaisalocados (se necessário) e distribuir 
    # os veículos conforme as prioridades das linhas-serviços.
    # Esse processo será feito nas seguinte situações:
    # 1) Se acima foram criados os registros de diário
    # 2) Foi retido um veículo
    # 3) Foi liberado um veículo
    # A análise dste método que foi criado é baseado nos horários de saída de garagem.
    # Isso resolver 99% dos casos da RS pois apenas uma linha 412-1 não é atendida.
    # Então nesse caso, o CCO tem que alocar o veículo manualmente.
    # Poderíamos ter definido esse registro como sendo saída de garagem e criado um novo
    # campo para definir quais saídas de garagem vão ter setor, mas como a linha 412-1 não
    # tem um veículo oficial, definiram deixar esse método atual pois atende as necessidades.
    # /////////////////////////////////////////////////////////////////////////////////////////
    # if True:
    if bvalidad and balocvei:
        # ////////////////////////////////////////////////////////////////////////////////////
        # Busca o último registro de automação para saber se o sistema esta em modo automático
        # ////////////////////////////////////////////////////////////////////////////////////
        sauxi001 = 'SELECT defmeto FROM abnf_operacional_movimentacao_programacao_automacao WHERE situreg != "C" ORDER BY dtmetod DESC LIMIT 1;'
        lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
        if lsqlre01 != [] and iqtdre01 > 0 and lsqlre01[0][0] == 'A':
            if ldatager == []: ldatager.append(ddataama)
            for ddataaux in ldatager:
                abnf_alert('Aguarde! Alocando veículos e setores nos registros de diário de programação do dia ' + abnf_converte_data(ddataaux) + '...', 15)
                # ////////////////////////////////////////////////
                # Pegando somente os registros de saida de garagem
                # ////////////////////////////////////////////////
                lcamposb = ('idoprdi', 'idolinh', 'veicpro', 'seghini', 'tipodia', 'veicger')
                lfilbusc = (('idfilia', '=', iidfilia), ('dataope', '=', ddataaux), ('saidgar', '=', True), ('situreg', '=', 'A'))
                lorderby = ('dataope', 'idolinh', 'veicpro')
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_diario', lcamposb, lfilbusc, lorderby)
                # Debug (início)
                # abnf_show('05', len(lsqlre01), 0)
                # abnf_show('06', lsqlre01, 1)
                # Debug (fim)
                if lsqlre01 != [] and iqtdre01 > 0:    # Existem registros da programação diária
                    # //////////////////////////////////////////////////////////////////////////////
                    # Guardando em memória os registros de diário de programação (lauxidia/lauxihor)
                    # //////////////////////////////////////////////////////////////////////////////
                    lauxidia = []
                    lauxihor = []
                    for lauxi001 in lsqlre01:
                        lauxidia.append([lauxi001[0], lauxi001[1], lauxi001[2], lauxi001[3], lauxi001[4], lauxi001[5], None, None, None])
                        lauxihor.append([lauxi001[3], lauxi001[0], None])
                    # ////////////////////////////////////////////////////////////////////////////////////
                    # Gerando dicionário de linhas com /informações de quantidade de portas e ar-condionado
                    # ///////////////////////////////////////////////////////////////////////////////////
                    # SELECT idolinh, qtporve, perqtpd, perveca, pervesa FROM abnf_operacional_cadastro_linhas;
                    dlinqpar = {}
                    lcamposb = ('idolinh', 'qtporve', 'perqtpd', 'perveca', 'pervesa')
                    lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '=', 'A'))
                    lorderby = ('idolinh', None)
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
                    for lauxi001 in lsqlre01:
                        dlinqpar[lauxi001[0]] = (lauxi001[1], lauxi001[2], lauxi001[3], lauxi001[4])
                    # Debug (início)
                    # abnf_show('05', dlinqpar, 2)
                    # Debug (fim)
                    # ///////////////////////////////////////////////////////////////////////////////////////
                    # Gerando dicionário de veículos com /informações de quantidade de portas e ar-condionado
                    # ///////////////////////////////////////////////////////////////////////////////////////
                    # SELECT idveicu, numport, arcondi FROM abnf_cadastro_veiculos;     
                    dveiqpar = {}
                    lcamposb = ('idveicu', 'numport', 'arcondi')
                    lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '=', 'A'))
                    lorderby = ('idveicu', None)
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                    for lauxi001 in lsqlre01:
                        dveiqpar[lauxi001[0]] = (lauxi001[1], lauxi001[2])
                    # Debug (início)
                    # abnf_show('06', dveiqpar, 2)
                    # Debug (fim)
                    # ///////////////////////////////////////////////////////////////////////////
                    # Guardando em memória os veículos que estão retidos com status 01 (lauxivre)
                    # ///////////////////////////////////////////////////////////////////////////
                    lauxivre = []
                    lcamposb = ('idveicu', None)
                    lfilbusc = (('idfilia', '=', iidfilia), ('statret', '=', 1), ('dataage', '<=', ddataama), ('dtliber', '[Null]'), ('situreg', '=', 'A'))
                    lorderby = ('idveicu', 'idoprrv')
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_retencao_veiculos', lcamposb, lfilbusc, lorderby)
                    for lauxi001 in lsqlre01:
                        if not lauxi001[0] in lauxivre:
                            lauxivre.append(lauxi001[0])
                    # Debug (início)
                    # abnf_show('05', lauxivre, 1)
                    # abnf_show('06', lsqlre01, 1)
                    # Debug (fim)
                    # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                    # Adicionando na memória os veículo que estão com status 02 e com a data de agendamento igual a data de hoje
                    # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                    lcamposb = ('idveicu', None)
                    lfilbusc = (('idfilia', '=', iidfilia), ('statret', '=', 2), ('dataage', '=', ddataama), ('dtliber', '[Null]'), ('situreg', '=', 'A'))
                    lorderby = ('idveicu', 'idoprrv')
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_retencao_veiculos', lcamposb, lfilbusc, lorderby)
                    for lauxi001 in lsqlre01:
                        if not lauxi001[0] in lauxivre:
                            lauxivre.append(lauxi001[0])
                    # Debug (início)
                    # abnf_show('07', lauxivre, 1)
                    # abnf_show('08', lsqlre01, 1)
                    # Debug (fim)
                    # //////////////////////////////////////////////////////
                    # Guardando em memória os setores de veículos (lauxiset)
                    # //////////////////////////////////////////////////////
                    lauxiset = []
                    lcamposb = ('idosetv', 'qtdveic')
                    lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '=', 'A'))
                    lorderby = ('ordprio', 'idosetv')
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_setor_veiculos', lcamposb, lfilbusc, lorderby)
                    for lauxi001 in lsqlre01:
                        lauxiset.append([lauxi001[0], lauxi001[1], 0])
                    # ///////////////////////////////////////////////////////////////////
                    # 1a Etapa => Distribuindo os veículos oficiais de cada linha-serviço
                    # ///////////////////////////////////////////////////////////////////
                    lcamposb = ('idoplin', 'ordprio', 'idolinh', 'veicser', 'idveicu', 'tpdiaut', 'tpdiasa', 'tpdiado', 'tpdiafe', 'tpdia2a', 'tpdia3a', 'tpdia4a', 'tpdia5a', 'tpdia6a')
                    lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '=', 'A'))
                    lorderby = ('ordprio', 'idoplin')
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] and iqtdre01 > 0:
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
                            for lauxi002 in lauxidia:                       # ('idoprdi', 'idolinh', 'veicpro', 'seghini', 'tipodia')
                                if lauxi002[1] == iidolinh:                 # Mesma linha
                                    if lauxi002[2] == iveicser:             # Mesmo serviço
                                        if lauxi002[4] in stipodia:         # Se o tipo de dia esta incluído dentro do registro de prioridade
                                            lauxi002[7] = iidveicu          # Define o veículo oficial
                                            if not iidveicu in lauxivre:    # Se o veículo não esta retido com status 01   
                                                lauxi002[6] = iidveicu      # Aloca o veículo na operação
                    # //////////////////////////////////////////////////////////////////////////////////////////////////////
                    # 2a Etapa => Distribuindo os veículos não-oficiais para cada registro que não recebeu o veículo oficial
                    # //////////////////////////////////////////////////////////////////////////////////////////////////////
                    with open("abnftmp/abnf000u13m2100a.log", 'w') as sarqutes:
                        if lsqlre01 != [] and iqtdre01 > 0:
                            for lauxi001 in lsqlre01:
                                iidoplin = lauxi001[0]
                                iordprio = lauxi001[1]
                                iidolinh = lauxi001[2]
                                iveicser = lauxi001[3]
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
                                # /////////////////////////////////////////////////////////
                                # Busca grupos de veículos vinculados ao registro principal
                                # /////////////////////////////////////////////////////////
                                sarqutes.write('======================================================================' + '\n')
                                sarqutes.write('[A00] iidoplin: ' + str(iidoplin) + '\n')
                                sarqutes.write('[A01] iordprio: ' + str(iordprio) + '\n')
                                sarqutes.write('[A02] iidolinh: ' + str(iidolinh) + '\n')
                                sarqutes.write('[A03] iveicser: ' + str(iveicser) + '\n')
                                sarqutes.write('[A04] stipodia: ' + str(stipodia) + '\n')
                                lcamposb = ('ordprio', 'idogrve')
                                lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'), None)
                                lorderby = (('idoplin', 'ordprio', 'idoplgv'))
                                lsqlre02, iqtdre02 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas_gv', lcamposb, lfilbusc, lorderby)
                                if lsqlre02 != [] and iqtdre02 > 0:
                                    for lauxi002 in lsqlre02:
                                        iordprio = lauxi002[0]
                                        iidogrve = lauxi002[1]
                                        lcamposb = ('idveicu', None)
                                        lfilbusc = (('idogrve', '=', iidogrve), ('situreg', '!=', 'C'), None)
                                        lorderby = (('idogrve', 'idveicu', 'idogrvv'))
                                        lsqlre03, iqtdre03 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
                                        if lsqlre03 != [] and iqtdre03 > 0:
                                            for lauxi003 in lsqlre03:
                                                iidveicu = lauxi003[0]
                                                sarqutes.write('----------------------------------------------------------------------' + '\n')
                                                sarqutes.write('[B00] iidveicu: ' + str(iidveicu) + '\n')
                                                sarqutes.write('[B01] lauxivre: ' + str(lauxivre) + '\n')
                                                if not iidveicu in lauxivre: # Se o veículo não esta retido
                                                    sarqutes.write('[B02] =======>: Veículo não esta retido!' + '\n')
                                                    # ////////////////////////////////////////////////////////////////////////////
                                                    # Verifica se o veículo ja não foi alocado em "lauxidia" em outra linha-seviço
                                                    # ////////////////////////////////////////////////////////////////////////////
                                                    bvalidad = True
                                                    for lauxi004 in lauxidia:                       # ('idoprdi', 'idolinh', 'veicpro', 'seghini', 'tipodia')
                                                        if lauxi004 [6] == iidveicu:
                                                            bvalidad = False
                                                            sarqutes.write('[B03] =======>: Veículo esta alocado!' + '\n')
                                                            break
                                                    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                    # Caso o veículo não foi alocado então busca a linha-serviço em "lauxidia" e aloca caso não tenha recebido nenhum veículo ainda
                                                    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                    if bvalidad:
                                                        sarqutes.write('[B04] =======>: Veículo não esta alocado!' + '\n')
                                                        for lauxi004 in lauxidia:                   # ('idoprdi', 'idolinh', 'veicpro', 'seghini', 'tipodia')
                                                            if lauxi004[1] == iidolinh:             # Mesma linha
                                                                if lauxi004[2] == iveicser:         # Mesmo serviço
                                                                    if lauxi004[4] in stipodia:     # Se o tipo de dia esta incluído dentro do registro de prioridade
                                                                        sarqutes.write('[C00] lauxi004: ' + str(lauxi004) + '\n')
                                                                        if lauxi004[6] == None:     # Se não tem veículo alocado
                                                                            sarqutes.write('[C01] =======>: Sem veículo!' + '\n')
                                                                            # /////////////////////////////////////////////////////////////
                                                                            # Validando o veículo pelos dicionários "dlinqpar" e "dveiqpar"
                                                                            # /////////////////////////////////////////////////////////////
                                                                            bvalidad = True
                                                                            if   dlinqpar == {} or dveiqpar == {}:                                                      bvalidad = False    # Alguns dos dicionários estarem vazios
                                                                            elif dlinqpar[iidolinh][0] != dveiqpar[iidveicu][0] and dlinqpar[iidolinh][1] == False:     bvalidad = False    # Quantidade de portas divergente e sem permissão de divergência
                                                                            elif dlinqpar[iidolinh][2] == False and dveiqpar[iidveicu][1] == True:                      bvalidad = False    # Linha não permite com ar-condicionado e veículo possui ar condicionado
                                                                            elif dlinqpar[iidolinh][3] == False and dveiqpar[iidveicu][1] == False:                     bvalidad = False    # Linha não permite sem ar-condicionado e veículo não possui ar condicionado
                                                                            if bvalidad:
                                                                                sarqutes.write('[D01] =======>: Veículo aprovado!' + '\n')
                                                                                lauxi004[6] = iidveicu  # Aloca o veículo
                                                                                sarqutes.write('[D02] lauxi004: ' + str(lauxi004) + '\n')
                    # ///////////////////////////////////////////////////////////////////
                    # 3a Etapa => Alocação de veículos nos registros de controle de setor
                    # Esse processo é feito analisando:
                    # 1) O horário de saída do veículo
                    # 2) A disponibilidade de quantidade de veículos do setor
                    # ///////////////////////////////////////////////////////////////////
                    lauxihor.sort()
                    for lauxi001 in lauxihor:
                        for lauxi002 in lauxiset:
                            if lauxi002[2] < lauxi002[1]:
                                lauxi001[2] = lauxi002[0]
                                lauxi002[2] += 1
                                break
                    for lauxi001 in lauxihor:
                        if lauxi001[2] != None:
                            for lauxi002 in lauxidia:
                                if lauxi002[0] == lauxi001[1]:
                                    lauxi002[8] = lauxi001[2]
                                    
                    # Debug (início)
                    # abnf_show('05', lauxiset, 1)
                    # abnf_show('06', lauxihor, 1)
                    # abnf_show('07', lauxidia, 1)
                    # Debug (fim)
                    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    # 4a Etapa => Atualização dos registros
                    # Atualizando em lote as informações de veículos e setores nos registros de diário de programação através de comando SQL
                    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    bvalidad = True
                    dauxi001 = {}
                    sauxi001 = ''
                    sauxi002 = ''
                    sauxi003 = ''
                    for lauxi001 in lauxidia:
                        iidoprdi = lauxi001[0]
                        iveicger = lauxi001[5]
                        iidveicu = lauxi001[6] if lauxi001[6] != None else 'NULL'
                        iidveofi = lauxi001[7] if lauxi001[7] != None else 'NULL'
                        iidosetv = lauxi001[8]
                        if dauxi001.get(iveicger, None) == None:
                            dauxi001[iveicger] = (iidveicu, iidveofi)
                            sauxi001 = sauxi001 + 'WHEN veicger = ' + str(iveicger) + ' THEN ' + str(iidveicu) + ' '        # + '<br>'  # <= Debug
                            sauxi002 = sauxi002 + 'WHEN veicger = ' + str(iveicger) + ' THEN ' + str(iidveofi) + ' '        # + '<br>'  # <= Debug
                        if iidosetv != None:                                                                            # 
                            sauxi003 = sauxi003 + 'WHEN idoprdi = ' + str(iidoprdi) + ' THEN ' + str(iidosetv) + ' '    # + '<br>'  # <= Debug
                        else:
                            if dauxi001[iveicger] != (iidveicu, iidveofi):
                                abnf_alert('Erro no dicionário de atualização de veículos! Entre em contato com o depto. de sistemas!', 4)
                                bvalidad = False
                                break
                    if bvalidad:
                        scommsql = 'UPDATE abnf_operacional_movimentacao_programacao_diario SET '   # + '<br>'  # <= Debug
                        # Veículo selecionado
                        scommsql = scommsql + 'idveicu = CASE '                                     # + '<br>'  # <= Debug
                        scommsql = scommsql +  sauxi001
                        scommsql = scommsql + 'ELSE NULL '                                          # + '<br>'  # <= Debug
                        scommsql = scommsql + 'END, '                                               # + '<br>'  # <= Debug
                        # Veículo oficial
                        scommsql = scommsql + 'idveofi = CASE '                                     # + '<br>'  # <= Debug
                        scommsql = scommsql +  sauxi002
                        scommsql = scommsql + 'ELSE NULL '                                          # + '<br>'  # <= Debug
                        scommsql = scommsql + 'END, '                                               # + '<br>'  # <= Debug
                        # Setor
                        scommsql = scommsql + 'idosetv = CASE '                                     # + '<br>'  # <= Debug
                        scommsql = scommsql +  sauxi003
                        scommsql = scommsql + 'ELSE NULL '                                          # + '<br>'  # <= Debug
                        scommsql = scommsql + 'END '                                                # + '<br>'  # <= Debug
                        scommsql = scommsql + 'WHERE dataope = "' + str(ddataaux) + '";'            # + '<br>'  # <= Debug
                        # Debug (início)
                        # abnf_show('05', scommsql, 0)
                        # Debug (fim)
                        # /////////////////////////////
                        # Alterando os registros do dia
                        # /////////////////////////////
                        bvalidad = abnf_database_executa_sql_commit(icodbase, sabnproj, scommsql, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                        if not bvalidad:
                            abnf_alert('Erro ao criar registros de retenção de veículos! Entre em contato com o depto. de sistemas!', 4)
                            break
                        else:
                            abnf_alert('Registros de diário de programação atualizados com sucesso para o dia ' + abnf_converte_data(ddataaux) + ' !', 3)
    # /////////////////////////////////////////////////////////////////
    # Cria as listas de veículo utilizados e retidos com status 01 e 02
    # /////////////////////////////////////////////////////////////////
    lidvehoj = []   # Veículo utilizados e retidos com status 01 e 02 na data de hoje
    lidveama = []   # Veículo utilizados e retidos com status 01 e 02 na data de amanhã
    # ///////////////////////////////////////////////////////////////////////////////////
    # Início da tela de linhas-serviços do dia de hoje e amanhã (grids da tela inicial)
    # Cada linha-serviço será tratada independente do veiculo oficial
    # O sistema deve mostrar os dados de cada linha-serviço basedo nas regras abaixo:
    # 1) Linha que o horário atual esta maior que o ultimo horário de chegada dessa linha
    #    Essa linha não deve aparecer na tela
    # 2) Linha que o horário atual esta menor que o ultimo horário de chegada dessa linha
    #    Aparecer o ultimo horário de saída dessa linha antes do horário atual
    # 3) Linha que o horário atual esta menor que o primeiro horário de saída dessa linha
    #    Aparecer o primeiro horário dessa linha que ainda não foi feito
    # ///////////////////////////////////////////////////////////////////////////////////
    shoraatu = abnf_websocket_date_time(4)                          # Horário atual (em HH:MM)
    ihoraatu = abnf_converte_hora_string_em_segundos(shoraatu)      # Horário atual (em segundos)
    # Simulação (início)
    # ihoraatu = (20 * 3600) + ( 0 * 60) # 20:00
    # ihoraatu = (21 * 3600) + (51 * 60) # 21:51
    # ihoraatu = (23 * 3600) + (59 * 60) # 23:59
    # Simulação (fim)
    for iauxi001 in range(2):
        if   iauxi001 == 0: lauxidia = [ddatahoj, 'sdivthoj', 'abnftr10', 'sdivthsv', 'abnftr11']
        elif iauxi001 == 1: lauxidia = [ddataama, 'sdivtama', 'abnftr20', 'sdivtasv', 'abnftr21']
        # ///////////////////////////////
        # Criação de dicionários e listas
        # ///////////////////////////////
        dprogrid = {}   # Dicionário de programação que será apresentando nas grids
        dprovger = {}   # Dicionário de programação dos veículos gerais
        llinsemv = []   # Linhas-serviços sem veículos
        # ////////////////////////////////////////////////
        # Dados de linhas-serviços do dia de hoje e amanhã
        # ////////////////////////////////////////////////
        sauxi001 = 'SELECT '
        # Campos das tabelas
        sauxi001 = sauxi001 + 'abnf01.codolin, '    # [00] Codigo da linha
        sauxi001 = sauxi001 + 'abnf02.veicpro, '    # [01] Veículo-Serviço
        sauxi001 = sauxi001 + 'abnf02.tipodia, '    # [02] Tipo de dia
        sauxi001 = sauxi001 + 'abnf02.idveicu, '    # [03] ID do veículo
        sauxi001 = sauxi001 + 'abnf04.prefvei, '    # [04] Prefixo do veículo
        sauxi001 = sauxi001 + 'abnf02.idveofi, '    # [05] ID do veículo oficial
        sauxi001 = sauxi001 + 'abnf05.descset, '    # [06] Descrição do setor        
        sauxi001 = sauxi001 + 'abnf02.seghini, '    # [07] Horário de início (em segundos)
        sauxi001 = sauxi001 + 'abnf02.seghfim, '    # [08] Horário de término (em segundos)
        sauxi001 = sauxi001 + 'abnf02.sentido, '    # [09] Sentido
        sauxi001 = sauxi001 + 'abnf03.desoloc, '    # [10] Descrição do local de origem
        sauxi001 = sauxi001 + 'abnf02.idotivi, '    # [11] Tipo de viagem: 1=Ocioso/2=Produtivo/3=Reservado/4=Deslocamento
        sauxi001 = sauxi001 + 'abnf01.qtporve, '    # [12] Quantidade padrão de portas dos veículos da linha
        sauxi001 = sauxi001 + 'abnf04.numport, '    # [13] Número de portas do veículo
        sauxi001 = sauxi001 + 'abnf01.perveca, '    # [14] Permite veículos com ar-condicionado
        sauxi001 = sauxi001 + 'abnf01.pervesa, '    # [15] Permite veículos sem ar-condicionado
        sauxi001 = sauxi001 + 'abnf04.arcondi, '    # [16] Veículo tem ar-condicionado?
        sauxi001 = sauxi001 + 'abnf02.veicger  '    # [17] Veículo geral
        # Tabelas SQL
        sauxi001 = sauxi001 + 'FROM       abnf_operacional_cadastro_linhas                 AS abnf01 '
        sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_programacao_diario AS abnf02 '
        sauxi001 = sauxi001 + 'ON         abnf01.idolinh = abnf02.idolinh '
        sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_locais                 AS abnf03 '
        sauxi001 = sauxi001 + 'ON         abnf02.idolori = abnf03.idoloca '
        sauxi001 = sauxi001 + 'LEFT JOIN  abnf_cadastro_veiculos                           AS abnf04 '
        sauxi001 = sauxi001 + 'ON         abnf02.idveicu = abnf04.idveicu '
        sauxi001 = sauxi001 + 'LEFT JOIN  abnf_operacional_cadastro_setor_veiculos         AS abnf05 '
        sauxi001 = sauxi001 + 'ON         abnf02.idosetv = abnf05.idosetv '
        # Condições SQL
        sauxi001 = sauxi001 + 'WHERE abnf01.situreg != "C" '                        # ==> Somente registros não cancelados (linhas)
        sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                        # ==> Somente registros não cancelados (diário)
        sauxi001 = sauxi001 + 'AND   abnf02.idfilia = ' + str(iidfilia) + ' '       # ==> Somente registros da filial
        sauxi001 = sauxi001 + 'AND   abnf02.dataope = "' + str(lauxidia[0]) + '" '  # ==> Somente registros da data em análise
        # Na primeira grid as informações serão organizadas baseadas em linha-serviço
        # Na primeira grid as informações serão organizadas baseadas no veículo geral
        if   iauxi001 == 0: sauxi001 = sauxi001 + 'ORDER BY abnf01.codolin, abnf02.veicpro, abnf02.seghini;'
        elif iauxi001 == 1: sauxi001 = sauxi001 + 'ORDER BY abnf02.veicger, abnf02.seghini;'
        # Execução
        lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
        # Debug (início)
        # abnf_show('05', sauxi001, 0)
        # if iauxi001 == 0: abnf_show('10', lsqlre01, 1)
        # Debug (fim)
        for lauxi001 in lsqlre01:
            scodolin = lauxi001[0]
            iveicpro = lauxi001[1]
            stipodia = lauxi001[2]
            iidveicu = lauxi001[3]
            sprefvei = lauxi001[4]
            iidveofi = lauxi001[5]
            sdescset = lauxi001[6]
            iseghini = lauxi001[7]
            iseghfim = lauxi001[8]
            ssentido = lauxi001[9]
            sdesoloc = lauxi001[10]
            iidotivi = lauxi001[11]
            iqtporve = lauxi001[12]
            inumport = lauxi001[13]
            bperveca = lauxi001[14]
            bpervesa = lauxi001[15]
            barcondi = lauxi001[16]
            iveicger = lauxi001[17]
            # /////////////////////////////////////////
            # Cria o dicionário de linha-serviço do dia
            # /////////////////////////////////////////
            if iauxi001 == 0 or dprovger.get((iveicger), None) == None:
                if dprogrid.get((scodolin, iveicpro), None) == None:
                    # [05] e [06] somente serão abastecidos na criação do dicionário
                    dprogrid[(scodolin, iveicpro)] = [
                        stipodia, # [00] Tipo de dia (variável)
                        iidveicu, # [01] Veiculo atual (variável)
                        sprefvei, # [02] Prefixo do veículo atual (variável)
                        iidveofi, # [03] Veiculo oficial (variável)
                        sdescset, # [04] Setor (variável)
                        iseghini, # [05] Primeiro horário inicial (fixo)
                        iseghfim, # [06] Primeiro horário final (fixo)
                        iseghini, # [07] Horário inicial do momento (variável)
                        iseghfim, # [08] Horário final do momento (variável)
                        iseghini, # [09] Último horário inicial (variável)
                        iseghfim, # [10] Último horário final (variável)
                        ssentido, # [11] Sentido atual (variável)
                        sdesoloc, # [12] Descrição do local atual (variável)
                        iidotivi, # [13] Tipo de viagem: 1=Ocioso/2=Produtivo/3=Reservado/4=Deslocamento (variável)
                        iqtporve, # [14] Quantidade padrão de portas dos veículos da linha (variável)
                        inumport, # [15] Número de portas do veículo atual (variável)
                        bperveca, # [16] Permite veículos com ar-condicionado (variável)
                        bpervesa, # [17] Permite veículos sem ar-condicionado (variável)
                        barcondi, # [18] Veículo atual tem ar-condicionado? (varíavel)
                        iveicger, # [19] Veículo geral
                    ]
                else:
                    # /////////////////////////////////////////////
                    # Atualiza o dicionário de linha-serviço do dia
                    # /////////////////////////////////////////////
                    if iauxi001 == 0:
                        # [09] e [10] serão os únicos campos que serão abastecidos em todo o momento
                        dprogrid[(scodolin, iveicpro)][9]  = iseghini # [09] Último horário inicial (variável)
                        dprogrid[(scodolin, iveicpro)][10] = iseghfim # [10] Último horário final (variável)
                        # Todos os demais campos serão abastecidos conforme o horário atual do dia (ihoraatu)
                        if ihoraatu >= iseghini:    # Se o horário atual for maior ou igual ao horário de inicio da viagem
                            dprogrid[(scodolin, iveicpro)][0]  = stipodia # [00] Tipo de dia (variável)
                            dprogrid[(scodolin, iveicpro)][1]  = iidveicu # [01] Veiculo atual (variável)
                            dprogrid[(scodolin, iveicpro)][2]  = sprefvei # [02] Prefixo do veículo atual (variável)
                            dprogrid[(scodolin, iveicpro)][3]  = iidveofi # [03] Veiculo oficial (variável)
                            dprogrid[(scodolin, iveicpro)][4]  = sdescset # [04] Setor (variável)
                            dprogrid[(scodolin, iveicpro)][7]  = iseghini # [07] Horário inicial do momento (variável)
                            dprogrid[(scodolin, iveicpro)][8]  = iseghfim # [08] Horário final do momento (variável)
                            dprogrid[(scodolin, iveicpro)][11] = ssentido # [11] Sentido atual (variável)
                            dprogrid[(scodolin, iveicpro)][12] = sdesoloc # [12] Descrição do local atual (variável)
                            dprogrid[(scodolin, iveicpro)][13] = iidotivi # [13] Tipo de viagem: 1=Ocioso/2=Produtivo/3=Reservado/4=Deslocamento (variável)
                            dprogrid[(scodolin, iveicpro)][14] = iqtporve # [14] Quantidade padrão de portas dos veículos da linha (variável)
                            dprogrid[(scodolin, iveicpro)][15] = inumport # [15] Número de portas do veículo atual (variável)
                            dprogrid[(scodolin, iveicpro)][16] = bperveca # [16] Permite veículos com ar-condicionado (variável)
                            dprogrid[(scodolin, iveicpro)][17] = bpervesa # [17] Permite veículos sem ar-condicionado (variável)
                            dprogrid[(scodolin, iveicpro)][18] = barcondi # [18] Veículo atual tem ar-condicionado? (varíavel)
                            dprogrid[(scodolin, iveicpro)][19] = iveicger # [19] Veículo geral
            # /////////////////////////////////////////////////////////////////////////////////////////////////
            # Cria o dicionário de veiculos gerais por dia
            # Esse dicionário vai ser usado para definir se a ultima viagem do veiculo geral estava sem veiculo
            # Se estiver, ele tem que incluir a linha-serviço na lista de linhas-serviços sem veículos
            # /////////////////////////////////////////////////////////////////////////////////////////////////
            if dprovger.get((iveicger), None) == None:
                # [00] e [01] somente serão abastecidos na criação do dicionário
                dprovger[(iveicger)] = [
                    iseghini, # [00] Horário inicial
                    scodolin, # [01] Código da linha
                    iveicpro, # [02] Serviço
                    iidveicu, # [03] Veiculo atual
                ]
            else:
                # ////////////////////////////////////////////////
                # Atualiza o dicionário de veiculos gerais por dia
                # ////////////////////////////////////////////////
                if iseghini >= dprovger[(iveicger)][0]:
                    dprovger[(iveicger)][0] = iseghini # [00] Horário inicial
                    dprovger[(iveicger)][1] = scodolin # [01] Código da linha
                    dprovger[(iveicger)][2] = iveicpro # [02] Serviço
                    dprovger[(iveicger)][3] = iidveicu # [03] Veiculo atual
            # ////////////////////////////////////////////////
            # Abastece a lista de linhas-serviços sem veículos
            # Pega somente os horários acima do horário atual
            # ////////////////////////////////////////////////
            if iidveicu == None:
                if iseghini >= ihoraatu:
                    if not (scodolin, iveicpro) in llinsemv:
                        llinsemv.append((scodolin, iveicpro))
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////
            # Analises feitas na data de hoje e em viagens que a data de termino estão maiores ou iguais a hora atual
            # ///////////////////////////////////////////////////////////////////////////////////////////////////////
            if lauxidia[0] == ddatahoj and iseghfim >= ihoraatu:
                # ///////////////////////////////////////////////////////
                # Abastece a lista de veículos utilizados na data de hoje
                # ///////////////////////////////////////////////////////
                if iidveicu != None:
                    if not iidveicu in lidvehoj:
                        lidvehoj.append(iidveicu)
            # /////////////////////////////////
            # Analises feitas na data de amanhã
            # /////////////////////////////////
            elif lauxidia[0] == ddataama:
                # /////////////////////////////////////////////////////////
                # Abastece a lista de veículos utilizados na data de amanhã
                # /////////////////////////////////////////////////////////
                if iidveicu != None:
                    if not iidveicu in lidveama:
                        lidveama.append(iidveicu)   
        # /////////////////////////////////////////////////////////////////////////////////////////
        # Varre o dicionário de veiculos gerais por dia procurando as linhas que estão sem veículos
        # Os que encontrar incluir a linha-serviço na lista de linhas-serviços sem veículos
        # /////////////////////////////////////////////////////////////////////////////////////////
        for lauxi001 in dprovger:
            if dprovger[lauxi001][3] == None:
                if not (dprovger[lauxi001][1], dprovger[lauxi001][2]) in llinsemv:
                    llinsemv.append((dprovger[lauxi001][1], dprovger[lauxi001][2]))
        # Debug (início)
        # if iauxi001 == 0: abnf_show('09', dprovger, 2)
        # if iauxi001 == 1: abnf_show('10', dprogrid, 2)
        # Debug (fim)
        # Rascunho (início)
        # retirado: 32536 - linha-serviço sem veículo: 004-1, 007-1 e 101-1
        # retirado: 32812 - linhas-serviço sem veículo: 328-1 e 826-1
        # ('0004', 1) - ['U', None, None, 775, None, 43500, 45300, 43500, 45300, 68400, 70080, 'I', 'TCI', 2, 2, None, 0, 1, None, 1003]
        # ('0007', 1) - ['U', 775, '32536', 775, None, 20400, 21780, 21780, 22680, 77880, 78660, 'V', 'RUA CORONEL JOAO MENDES P. DE ALMEIDA, 203', 2, 2, 2, 0, 1, 0, 1003]
        # ('0412', 1) - ['U', None, None, None, None, 16140, 16560, 29400, 31500, 88020, 88260, 'V', 'RUA BELO HORIZONTE', 2, 2, None, 0, 1, None, 1105]
        # ('0826', 1) - ['U', None, None, 747, None, 20700, 23100, 31260, 33660, 69000, 71400, 'V', 'TPA', 2, 2, None, 0, 1, None, 1090]
        # 23:59 não é para desaparecer nem a 328-1 e nem a 101-1
        # ('0101', 1) - ['U', None, None, 775, None, 17100, 18480, 30180, 31800, 84180, 85200, 'I', 'TCI', 2, 2, None, 0, 1, None, 1003]
        # 1003 - [26580, 28380, 24780, 26280, 84180, 85200]
        # ('0328', 1) - ['U', None, None, 747, None, 16020, 17400, 29580, 30960, 79500, 80580, 'V', 'TSJ', 2, 2, None, 0, 1, None, 1090]
        # 1090 - [16020, 17400, 69000, 71400, 79500, 80580]
        # Rascunho (fim)    
        # ////////////////////////////////////////////////
        # Dados de linhas-serviços do dia de hoje e amanhã
        # ////////////////////////////////////////////////
        lnewpage = [
            ('table-2', 'table table-bordered table-sm table-responsive border-secondary', 1, 1200, 300, None, None),
                ('tr-0', None, False),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Linha',    'form-control-label'),                                                ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Serviço',  'form-control-label'),                                                ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Tipo dia', 'form-control-label'),                                                ('td-9', None),
                    ('td-0', 'table-active', 2, None, 1, None, None), ('label-0', 'Veículo',  'form-control-label'),                                                ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Setor',    'form-control-label'),                                                ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Partida',  'form-control-label'),                                                ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'S',        'form-control-label', 'Sentido'),                                     ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Origem',   'form-control-label'),                                                ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'TV',       'form-control-label', 'Tipo de viagem'),                              ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'PL',       'form-control-label', 'Portas linha'),                                ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'PV',       'form-control-label', 'Portas veículo'),                              ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'AC',       'form-control-label', 'Linha permite veículos com ar condicionado?'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'AS',       'form-control-label', 'Linha permite veículos sem ar condicionado?'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'AV',       'form-control-label', 'Veículo possui ar condicionado?'),             ('td-9', None),
                ('tr-9', None)
        ]
        icontd01 = 0
        for lauxi001 in sorted(dprogrid):
            scodolin = lauxi001[0]
            iveicpro = lauxi001[1]
            stipodia = dprogrid[lauxi001][0]
            iidveicu = dprogrid[lauxi001][1]
            # iidveicu = None
            sprefvei = dprogrid[lauxi001][2]
            iidveofi = dprogrid[lauxi001][3]
            sdescset = dprogrid[lauxi001][4] if dprogrid[lauxi001][4] != None else '&nbsp;'
            iseghi00 = dprogrid[lauxi001][5]    # horario de início da primeira viagem
            iseghf00 = dprogrid[lauxi001][6]    # horario de término da primeira viagem
            iseghini = dprogrid[lauxi001][7]    # horario de início da viagem atual
            hseghini = abnf_converte_segundos_em_hora_string(iseghini, True)
            iseghfim = dprogrid[lauxi001][8]    # horario de término da viagem atual
            iseghi99 = dprogrid[lauxi001][9]    # horario de início da última viagem
            iseghf99 = dprogrid[lauxi001][10]   # horario de término da última viagem
            ssentido = dprogrid[lauxi001][11]
            sdesoloc = dprogrid[lauxi001][12]
            sidotivi = abnf_personal_retorna_string(10133, dprogrid[lauxi001][13])
            iqtporve = dprogrid[lauxi001][14]
            inumport = dprogrid[lauxi001][15] if dprogrid[lauxi001][15] != None else 0
            bperveca = dprogrid[lauxi001][16]
            bpervesa = dprogrid[lauxi001][17]
            barcondi = dprogrid[lauxi001][18]
            if iseghini <= iseghf99:    # Se o horário de inicio do viagem atual for menor ou igual ao horario de término da última viagem
                lcodolin = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'black', scodolin), ('td-9', None), ('tr-9', None), ('table-9', None)]
                lveicpro = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'black', iveicpro), ('td-9', None), ('tr-9', None), ('table-9', None)]
                ltipodia = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'black', stipodia), ('td-9', None), ('tr-9', None), ('table-9', None)]
                lauxi002 = ('yellow', 'black', '[Sem&nbsp;veículo]') if iidveicu == None else (None, 'black', sprefvei)
                lprefvei = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, lauxi002[0]), ('font-0', 'Courier New;', '16px', lauxi002[1], lauxi002[2]), ('td-9', None), ('tr-9', None), ('table-9', None)]
                lauxi002 = ('yellow', 'black', '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', '') if iidveicu == None else (None, 'green', 'OFI', 'Veículo oficial') if iidveicu == iidveofi else (None, 'red', 'SUB', 'Veículo substituto')
                lvofisub = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, lauxi002[0]), ('font-0', 'Courier New;', '16px', lauxi002[1], lauxi002[2], None, lauxi002[3]), ('td-9', None), ('tr-9', None), ('table-9', None)]
                ldescset = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', 'black', sdescset), ('td-9', None), ('tr-9', None), ('table-9', None)]
                lseghini = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'black', hseghini), ('td-9', None), ('tr-9', None), ('table-9', None)]
                sauxi001 = 'IDA' if ssentido == 'I' else 'VOLTA' if ssentido == 'V' else ''
                lsentido = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'black', ssentido, None, sauxi001), ('td-9', None), ('tr-9', None), ('table-9', None)]
                ldesoloc = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', 'black', sdesoloc), ('td-9', None), ('tr-9', None), ('table-9', None)]
                lidotivi = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'black', sidotivi[:2], None, sidotivi), ('td-9', None), ('tr-9', None), ('table-9', None)]
                sauxi001 = None if inumport >= iqtporve else 'yellow'
                sauxi002 = 'Quantidade de portas para a linha: ' + str(iqtporve)
                lqtporve = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, sauxi001), ('font-0', 'Courier New;', '16px', 'black', iqtporve, None, sauxi002), ('td-9', None), ('tr-9', None), ('table-9', None)]
                sauxi002 = 'Quantidade de portas do veículo: ' + str(inumport)
                lnumport = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, sauxi001), ('font-0', 'Courier New;', '16px', 'black', inumport, None, sauxi002), ('td-9', None), ('tr-9', None), ('table-9', None)]
                sauxi001 = 'yellow' if ((bperveca == False and barcondi == True) or (bperveca == True and barcondi == False)) else None
                sauxi002, sauxi003 = ('S','A linha permite veículos com ar-condicionado') if bperveca else ('N','A linha não permite veículos com ar-condicionado')
                lperveca = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, sauxi001), ('font-0', 'Courier New;', '16px', 'black', sauxi002, None, sauxi003), ('td-9', None), ('tr-9', None), ('table-9', None)]
                sauxi001 = 'yellow' if bpervesa == False and barcondi == False else None
                sauxi002, sauxi003 = ('S','A linha permite veículos sem ar-condicionado') if bpervesa else ('N','A linha não permite veículos sem ar-condicionado')
                lpervesa = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, sauxi001), ('font-0', 'Courier New;', '16px', 'black', sauxi002, None, sauxi003), ('td-9', None), ('tr-9', None), ('table-9', None)]
                sauxi001 = 'yellow' if ((bperveca == False and barcondi == True) or (bperveca == True and barcondi == False) or (bpervesa == False and barcondi == False)) else None
                sauxi002, sauxi003 = ('S','Veículo possui ar condicionado') if barcondi else ('N','Veículo não possui ar condicionado')
                larcondi = [('table-3', 1), ('tr-0', None, False), ('td-0', None, 1, None, 1, None, sauxi001), ('font-0', 'Courier New;', '16px', 'black', sauxi002, None, sauxi003), ('td-9', None), ('tr-9', None), ('table-9', None)]
                lnewpage = lnewpage + [
                    ('tr-0', None, True),
                        ('td-0', None, 1, None, 1, None, None)] + lcodolin +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lveicpro +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + ltipodia +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lprefvei +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lvofisub +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + ldescset +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lseghini +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lsentido +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + ldesoloc +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lidotivi +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lqtporve +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lnumport +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lperveca +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + lpervesa +  [('td-9', None),
                        ('td-0', None, 1, None, 1, None, None)] + larcondi +  [('td-9', None),
                        ('tr-9', None)
                ]
        lnewpage = lnewpage + [
            ('table-9', None),
            ('div-9', None),    # <== Esse 'div-9' é uma necessidade pelo uso de 'table-2'.
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, lauxidia[1], snewpage])        
        # ////////////////////////////
        # Linhas-serviços sem veículos
        # ////////////////////////////
        llinsemv.sort()
        if llinsemv != []:
            lnewpage = [
                ('table-0', 'table table-bordered table-sm table-responsive border-secondary')
            ]
            sauxi001 = ''
            for lauxi001 in llinsemv:
                scodolin = lauxi001[0]
                iveicpro = lauxi001[1]
                if sauxi001 != '':
                    sauxi001 = sauxi001 + ' '
                sauxi001 = sauxi001 + scodolin + '-' + str(iveicpro)
            lnewpage = lnewpage + [
                ('tr-0', None, False),
                    ('td-0', 'text-white bg-warning', 1, None, 1, None, None), ('font-0', 'Courier New;', '18px', 'black','Linhas-serviços sem veículos'), ('td-9', None),
                ('tr-9', None),
                ('tr-0', None, False),
                    ('td-0', None, 2, None, 0, None, None), ('font-0', 'Courier New;', '16px', 'black', sauxi001), ('td-9', None),
                ('tr-9', None),
            ]
            lnewpage = lnewpage + [
                ('table-9', None),
            ]
            snewpage = abnf_create_page(lnewpage)
            abnf_socket_004([1, lauxidia[3], snewpage])
    # /////////////////////////////////////////////////////////////////////
    # Informação sobre o método de geração automática de escala de veículos
    # /////////////////////////////////////////////////////////////////////
    sauxi001 = 'SELECT defmeto FROM abnf_operacional_movimentacao_programacao_automacao WHERE situreg != "C" ORDER BY dtmetod DESC LIMIT 1;'
    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)    
    if   lsqlre01 == [] or iqtdre01 == 0: lauxi001 = ('Não foi possível definir a geração automática de escala de veículos!<br>Entre em contato com o depto. de sistemas!', 'black', 'warning')
    elif lsqlre01[0][0] == 'M':           lauxi001 = ('A geração automática de escala de veículos esta desativada!', 'white', 'danger')
    elif lsqlre01[0][0] == 'A':           lauxi001 = ('A geração automática de escala de veículos esta ativada!', 'white', 'success')
    lnewpage = [
        ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
            ('tr-0', 'text-white bg-' + lauxi001[2] , False),
                ('td-0', None, 1, None, 1, None, None),
                    ('font-0', 'Courier New;', '20px', lauxi001[1], lauxi001[0]),
                ('td-9', None),
            ('tr-9', None),
        ('table-9', None),
    ]
    snewpage = abnf_create_page(lnewpage)
    abnf_socket_004([1, 'sdivtaut', snewpage])
    # //////////////////////////////////
    # Início da tela de veículos retidos
    # //////////////////////////////////
    for icontd01 in range(4):
        lauxi001 = [
            ('table-2', 'table table-bordered table-sm table-responsive border-secondary', 1, 1200, 200, 'abnftr3' + str(icontd01 + 1), 'lightgreen'),
                ('tr-0', None, False),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Data',               'form-control-label'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Hora',               'form-control-label'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Controle',           'form-control-label'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Veiculo',            'form-control-label'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Motivo',             'form-control-label'), ('td-9', None),
                    ('td-0', 'table-active', 3, None, 1, None, None), ('label-0', 'GSD',                'form-control-label'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Usuário que reteve', 'form-control-label'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('td-9', None),
                ('tr-9', None)
        ]
        if   icontd01 == 0: lnewpvr1 = lauxi001
        elif icontd01 == 1: lnewpvr2 = lauxi001
        elif icontd01 == 2: lnewpvr3 = lauxi001
        elif icontd01 == 3: lnewpvr4 = lauxi001
    # /////////////////////////////////////////////////////
    # Definição dos veículos que estão retidos e os motivos
    # /////////////////////////////////////////////////////
    sauxi001 = 'SELECT '
    # Campos das tabelas
    sauxi001 = sauxi001 + 'abnf01.idoprrv, '    # [00] ID do registro de controle de retenção do veículos
    sauxi001 = sauxi001 + 'abnf01.statret, '    # [01] Status da retenção
    sauxi001 = sauxi001 + 'abnf01.dataage, '    # [02] Data do agendamento
    sauxi001 = sauxi001 + 'abnf01.seghage, '    # [03] Hora do agendamento
    sauxi001 = sauxi001 + 'abnf01.codctrl, '    # [04] Código de controle
    sauxi001 = sauxi001 + 'abnf02.idveicu, '    # [05] ID do veículo
    sauxi001 = sauxi001 + 'abnf02.prefvei, '    # [06] Prefixo do veículo
    sauxi001 = sauxi001 + 'abnf01.descrre, '    # [07] Motivo da retenção
    sauxi001 = sauxi001 + 'abnf06.dessdeg, '    # [08] Descricao do grupo de GSD
    sauxi001 = sauxi001 + 'abnf05.dessdes, '    # [09] Descrição do subgrupo de GSD
    sauxi001 = sauxi001 + 'abnf04.dessded, '    # [10] Descrição da definição de GSD
    sauxi001 = sauxi001 + 'abnf03.nomeusu  '    # [11] Usuário que realizou a retenção
    # Tabela de retenção
    sauxi001 = sauxi001 + 'FROM abnf_operacional_movimentacao_programacao_retencao_veiculos AS abnf01 '
    # Tabela de veículos
    sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos                                AS abnf02 '
    sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
    # Tabela de usuário (usuário que reteve)
    sauxi001 = sauxi001 + 'INNER JOIN abnf_sistema_usuarios                                 AS abnf03 '
    sauxi001 = sauxi001 + 'ON         abnf01.idcusre = abnf03.idusuar '
    # Tabela definição de GSD
    sauxi001 = sauxi001 + 'LEFT JOIN abnf_sigom_cadastro_defeitos_definicoes                AS abnf04 '
    sauxi001 = sauxi001 + 'ON        abnf01.idsdede = abnf04.idsdede '
    # Tabela de subgrupos de GSD
    sauxi001 = sauxi001 + 'LEFT JOIN abnf_sigom_cadastro_defeitos_subgrupos                 AS abnf05 '
    sauxi001 = sauxi001 + 'ON        abnf04.idsdesg = abnf05.idsdesg '
    # Tabela de grupo de GSD
    sauxi001 = sauxi001 + 'LEFT JOIN abnf_sigom_cadastro_defeitos_grupos                    AS abnf06 '
    sauxi001 = sauxi001 + 'ON        abnf05.idsdegr = abnf06.idsdegr '
    # Cláusula WHERE
    sauxi001 = sauxi001 + 'WHERE '
    sauxi001 = sauxi001 + 'abnf01.situreg != "C" AND '                      # ==> Somente registros não cancelados (retenção)
    sauxi001 = sauxi001 + 'abnf01.idfilia = ' + str(iidfilia) + ' AND '     # ==> Somente registros da filial
    sauxi001 = sauxi001 + 'abnf01.dtliber IS NULL '
    # Ordenação
    # (28/08/2025 - Alterado a busca pela data do agendamento # sauxi001) sauxi001 = sauxi001 + 'ORDER BY abnf01.dtreten, abnf02.prefvei;'
    sauxi001 = sauxi001 + 'ORDER BY abnf01.dataage, abnf01.seghage, abnf02.prefvei, abnf01.dtreten;'
    # Execução
    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
    # Debug (início)
    # abnf_show('05', sauxi001, 0)
    # abnf_show('06', lsqlre01, 1)
    # Debug (fim)
    # ///////////////////////////////////
    # Abastece a tela de veículos retidos
    # ///////////////////////////////////
    lqtdver1 = []
    lqtdver2 = []
    lqtdver3 = [] 
    lqtdver4 = []
    if lsqlre01 != [] and iqtdre01 > 0:
        for lauxi001 in lsqlre01:
            iidoprrv = lauxi001[0]
            istatret = lauxi001[1]
            ddataage = lauxi001[2]
            sdataage = abnf_converte_data(ddataage)
            hseghage = abnf_converte_segundos_em_hora_string(lauxi001[3], False)
            scodctrl = str(1000000 + lauxi001[4])[1:]
            iidveicu = lauxi001[5]
            sprefvei = lauxi001[6]
            sdescrre = lauxi001[7]
            sdessdeg = lauxi001[8] if lauxi001[8] != None else ''
            sdessdes = lauxi001[9] if lauxi001[9] != None else ''
            sdessded = lauxi001[10] if lauxi001[10] != None else ''
            snomeure = lauxi001[11]
            lauxi002 = [
                ('tr-0', None, False),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'blue',  sdataage), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'blue',  hseghage), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'blue',  scodctrl), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'brown', sprefvei), ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', None,    sdescrre), ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', None,    sdessdeg), ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', None,    sdessdes), ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', None,    sdessded), ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', None,    snomeure), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('radio-0', 'iidoprrv', iidoprrv, None, 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                ('tr-9', None)
            ]
            if istatret == 1:
                lnewpvr1 = lnewpvr1 + lauxi002
                if not iidveicu in lqtdver1:
                    lqtdver1.append(iidveicu)
                if ddataage <= ddatahoj:
                    if not iidveicu in lidvehoj:
                        lidvehoj.append(iidveicu)
                if ddataage <= ddataama:
                    if not iidveicu in lidveama:
                        lidveama.append(iidveicu)
            elif istatret == 2:
                lnewpvr2 = lnewpvr2 + lauxi002
                if not iidveicu in lqtdver2:
                    lqtdver2.append(iidveicu)
                if ddataage <= ddatahoj:
                    if not iidveicu in lidvehoj:
                        lidvehoj.append(iidveicu)
                if ddataage <= ddataama:
                    if not iidveicu in lidveama:
                        lidveama.append(iidveicu)
            elif istatret == 3:
                lnewpvr3 = lnewpvr3 + lauxi002
                if not iidveicu in lqtdver3:
                    lqtdver3.append(iidveicu)
            elif istatret == 4:
                lnewpvr4 = lnewpvr4 + lauxi002
                if not iidveicu in lqtdver4:
                    lqtdver4.append(iidveicu)
    lauxi001 = [
        ('table-9', None),
        ('div-9', None),    # <== Esse 'div-9' é uma necessidade pelo uso de 'table-2'.
    ]
    lnewpvr1 = lnewpvr1 + lauxi001
    lnewpvr2 = lnewpvr2 + lauxi001
    lnewpvr3 = lnewpvr3 + lauxi001
    lnewpvr4 = lnewpvr4 + lauxi001
    snewpage = abnf_create_page(lnewpvr1)
    abnf_socket_004([1, 'sdivtvr1', snewpage])
    sauxi001 = '</font><font color=black FACE="Courier New" size=4><b>' + str(len(lqtdver1)) + '</b></font>'
    abnf_socket_004([1, 'sdivttv1', sauxi001])
    snewpage = abnf_create_page(lnewpvr2)
    abnf_socket_004([1, 'sdivtvr2', snewpage])
    sauxi001 = '</font><font color=black FACE="Courier New" size=4><b>' + str(len(lqtdver2)) + '</b></font>'
    abnf_socket_004([1, 'sdivttv2', sauxi001])
    snewpage = abnf_create_page(lnewpvr3)
    abnf_socket_004([1, 'sdivtvr3', snewpage])
    sauxi001 = '</font><font color=black FACE="Courier New" size=4><b>' + str(len(lqtdver3)) + '</b></font>'
    abnf_socket_004([1, 'sdivttv3', sauxi001])
    snewpage = abnf_create_page(lnewpvr4)
    abnf_socket_004([1, 'sdivtvr4', snewpage])
    sauxi001 = '</font><font color=black FACE="Courier New" size=4><b>' + str(len(lqtdver4)) + '</b></font>'
    abnf_socket_004([1, 'sdivttv4', sauxi001])
    # /////////////////////////////////////////////////////////////////////////////////
    # Atualiza os veículos que não foram utilizados na data de hoje e na data de amanhã
    # /////////////////////////////////////////////////////////////////////////////////
    # Debug (início)
    # abnf_show('05', lidvehoj, 1)
    # abnf_show('07', lidveama, 1)
    # Debug (fim)
    for lauxi001 in ((lidvehoj, 'sdivthvn'), (lidveama, 'sdivtavn')):
        if lauxi001[0] != []:
            lnewpage = [
                ('table-0', 'table table-bordered table-sm table-responsive border-secondary')
            ]
            lcamposb = ('prefvei', None)
            lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '=', 'A'), ('veielev', '!=', True), ('idveicu', '[NotInList]', list(lauxi001[0])))
            lorderby = ('prefvei', 'idveicu')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
            sauxi001 = ''
            for lauxi002 in lsqlre01:
                sprefvei = lauxi002[0]
                if sauxi001 != '':
                    sauxi001 = sauxi001 + ' '
                sauxi001 = sauxi001 + sprefvei
            sauxi002 = ' a partir de ' + shoraatu if lauxi001[1] == 'sdivthvn' else ''
            lnewpage = lnewpage + [
                ('tr-0', None, False),
                    ('td-0', 'text-white bg-warning', 1, None, 1, None, None), ('font-0', 'Courier New;', '18px', 'black','Veículos não utilizados ' + sauxi002  + ' e não retidos com status 01 e 02'), ('td-9', None),
                ('tr-9', None),
                ('tr-0', None, False),
                    ('td-0', None, 2, None, 0, None, None), ('font-0', 'Courier New;', '16px', 'black', sauxi001), ('td-9', None),
                ('tr-9', None),
            ]
            lnewpage = lnewpage + [
                ('table-9', None),
            ]
            snewpage = abnf_create_page(lnewpage)
            abnf_socket_004([1, lauxi001[1], snewpage])
    # ////////////////////////////////////////////////
    # Atualiza a data da ultima atualição no cabeçalho
    # ////////////////////////////////////////////////
    sauxi001 = '<font color=white size=5>Última atualização: </font><font color=#E8BD84 FACE="Courier New" size=5><b>' + abnf_converte_datahora(datetime.now(), 0) + '</b></font>'
    abnf_socket_004([1, 'sdivulat', sauxi001])
    if bvalidad:
        abnf_alert('Informações atualizadas com sucesso!', 3)
    # ////////////////////////////////
    # Habilita todos os botões do form
    # ////////////////////////////////
    for sauxi001 in lbuttfor:
        abnf_socket_004([5, sauxi001])      # Habilita o botão
    # ///////////////////////////////////////
    # Exclui o arquivo temporário de bloqueio
    # ///////////////////////////////////////
    try:
        os.remove(sarqdown)
    except:
        pass
    if os.path.isfile(sarqdown):
        abnf_alert('Erro ao excluir o arquivo de bloqueio! Entre em contato com o depto. de sistemas!', 4)
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13m02104_operacional_programacao_movimentacao_controle_diario ] //////////////////////////////////////////////////////////////////////////// #
# // Programação - Controle Diário.                                                                                                                      // #
# // Relatórios.                                                                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13m02104_operacional_programacao_movimentacao_controle_diario(dabnfopg, irelator, ddataini, ihoraini, ddatafim, ihorafim,
    iidveicu, iidsdede, bstatu01, bstatu02, bstatu03, bstatu04, ddats01i, ddats01f, ddats02i, ddats02f, ddats03i, ddats03f, ddats04i, ddats04f, iformrel):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13m02104_operacional_programacao_movimentacao_controle_diario(...)')
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
        if   irelator in (1, 2, 3): icolspan = 10
        elif irelator == 4:         icolspan = 4
        elif irelator == 5:         icolspan = 1
        elif irelator in (6, 7):    icolspan = 10
        elif irelator == 8:         icolspan = 12
        elif irelator == 9:         icolspan = 3
        elif irelator == 10:        icolspan = 14
        elif irelator == 11:        icolspan = 11
        ifontlen = 2
        icontreg = 0
        # ////////////////////
        # Listas e dicionários
        # ////////////////////
        drelator = {
             0: '',
             1: '01 - SAÍDA DE GARAGEM - GERAL',
             2: '02 - SAÍDA DE GARAGEM - VEÍCULOS COM SETORES',
             3: '03 - SAÍDA DE GARAGEM - VEÍCULOS SEM SETORES',
             4: '04 - SAÍDA DE GARAGEM - VEÍCULOS POR SETORES',
             5: '05 - SAÍDA DE GARAGEM - SETORES POR VEÍCULOS',
             6: '06 - DIARIO POR LINHA-SERVIÇO',
             7: '07 - DIARIO POR VEÍCULO',
             8: '08 - SUBSTITUÍÇÃO DE VEÍCULOS',
             9: '09 - VEÍCULOS NÃO UTILIZADOS E VEÍCULOS RETIDOS',
            10: '10 - RETENÇÃO E LIBERAÇÃO DE VEÍCULOS',
            11: '11 - DIÁRIO DA MANUTENÇÃO',
            # 12: '12 - STATUS DIÁRIO DA MANUTENÇÃO - MODELO 02',
        }
        # ///////////////////
        # Gerando o relatório
        # ///////////////////
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'PROGRAMAÇÃO - ' + drelator[irelator])
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            if irelator != 11:
                smensage = 'Período: ' + abnf_converte_data(ddataini) + ' até ' + abnf_converte_data(ddatafim)
                abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            if irelator in (1, 2, 3):
                # ////////////////////////////////////////////
                # 01 - SAÍDA DE GARAGEM - GERAL
                # 02 - SAÍDA DE GARAGEM - VEÍCULOS COM SETORES
                # 03 - SAÍDA DE GARAGEM - VEÍCULOS SEM SETORES
                # ////////////////////////////////////////////
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_info_001(sarquwri, '#B1C8C9', 'center', 1,
                    [
                        ('Linha',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Serv',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Veíc',   2, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Setor',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Obs',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('TD',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Hor',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('S',      1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Origem', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_fthead_tbody(sarquwri)
                ddataaux = ddataini
                while ddataaux <= ddatafim:
                    lprefvei = []   # Lista de veículos usados no dia
                    dveicger = {}   # Dicionário para definir se o veículo geral esta iniciando na garagem (caso não iniciar então ele é EXTERNO)
                    lretidos = []   # Lista de veículos retidos
                    # /////////////////
                    # Cabeçalho por dia
                    # /////////////////
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    abnf_imprime_info_001(sarquwri, '#8EDADE', 'center', 1,
                        [
                            (abnf_converte_data(ddataaux), icolspan, 0, None, None, 'black', 'Courier New', ifontlen + 2, True, False),
                        ]
                    )
                    abnf_imprime_info_001(sarquwri, '#B1C8C9', 'center', 1,
                        [
                            ('Linha',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Serv',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Veíc',   2, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Setor',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Obs',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('TD',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Hor',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('S',      1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Origem', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    # ///////////////////////////////////////////
                    # Dados de linhas-serviços da data em análise
                    # ///////////////////////////////////////////
                    sauxi001 = 'SELECT '
                    # Campos das tabelas
                    sauxi001 = sauxi001 + 'abnf01.codolin, '    # [00] Codigo da linha
                    sauxi001 = sauxi001 + 'abnf02.veicpro, '    # [01] Veículo-Serviço
                    sauxi001 = sauxi001 + 'abnf02.tipodia, '    # [02] Tipo de dia
                    sauxi001 = sauxi001 + 'abnf02.seghini, '    # [03] Horário de início (em segundos)
                    sauxi001 = sauxi001 + 'abnf02.sentido, '    # [04] Sentido
                    sauxi001 = sauxi001 + 'abnf03.desoloc, '    # [05] Descrição do local de origem
                    sauxi001 = sauxi001 + 'abnf02.idveicu, '    # [06] ID do veículo
                    sauxi001 = sauxi001 + 'abnf04.prefvei, '    # [07] Prefixo do veículo
                    sauxi001 = sauxi001 + 'abnf02.idveofi, '    # [08] ID do veículo oficial
                    sauxi001 = sauxi001 + 'abnf05.descset, '    # [09] Descrição do setor
                    sauxi001 = sauxi001 + 'abnf01.qtporve, '    # [10] Quantidade padrão de portas dos veículos da linha
                    sauxi001 = sauxi001 + 'abnf01.perqtpd, '    # [11] Permite veículos com quantidade de portas divergente do padrão
                    sauxi001 = sauxi001 + 'abnf01.perveca, '    # [12] Permite veículos com ar-condicionado
                    sauxi001 = sauxi001 + 'abnf01.pervesa, '    # [13] Permite veículos sem ar-condicionado
                    sauxi001 = sauxi001 + 'abnf04.numport, '    # [14] Número de portas do veículo
                    sauxi001 = sauxi001 + 'abnf04.arcondi, '    # [15] Veículo tem ar-condicionado?
                    sauxi001 = sauxi001 + 'abnf02.saidgar, '    # [16] Saida de garagem?
                    sauxi001 = sauxi001 + 'abnf02.veicger  '    # [17] Veículo geral
                    # Tabelas SQL
                    sauxi001 = sauxi001 + 'FROM       abnf_operacional_cadastro_linhas                 AS abnf01 '
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_programacao_diario AS abnf02 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idolinh = abnf02.idolinh '
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_locais                 AS abnf03 '
                    sauxi001 = sauxi001 + 'ON         abnf02.idolori = abnf03.idoloca '
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_cadastro_veiculos                           AS abnf04 '
                    sauxi001 = sauxi001 + 'ON         abnf02.idveicu = abnf04.idveicu '
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_operacional_cadastro_setor_veiculos         AS abnf05 '
                    sauxi001 = sauxi001 + 'ON         abnf02.idosetv = abnf05.idosetv '
                    # Condições SQL
                    sauxi001 = sauxi001 + 'WHERE abnf01.situreg != "C" '                    # ==> Somente registros não cancelados (linhas)
                    sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                    # ==> Somente registros não cancelados (diário)
                    sauxi001 = sauxi001 + 'AND   abnf02.idfilia = ' + str(iidfilia) + ' '   # ==> Somente registros da filial
                    sauxi001 = sauxi001 + 'AND   abnf02.dataope = "' + str(ddataaux) + '" ' # ==> Somente registros da data em análise
                    # Ordenação
                    sauxi001 = sauxi001 + 'ORDER BY abnf01.codolin, abnf02.veicpro, abnf02.seghini;'
                    # Execução
                    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                    # Debug (início)
                    # abnf_show('05', sauxi001, 0)
                    # abnf_show('06', lsqlre01, 1)
                    # Debug (fim)
                    slinsvei = ''
                    sauxi003 = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                    bbprviag = False                # Não busca a primeira viagem após saída da garagem
                    for lauxi001 in lsqlre01:
                        iseghini = lauxi001[3]
                        bsaidgar = lauxi001[16]
                        iveicger = lauxi001[17]
                        sprefvei = lauxi001[7] if lauxi001[7] != None else ''
                        # //////////////////////
                        # Abastecendo 'lprefvei'
                        # //////////////////////
                        if sprefvei != '' and not sprefvei in lprefvei:
                            lprefvei.append(sprefvei)
                        # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                        # Abastecendo 'dveicger' com o horário menor de saída que tiver e com a informação se esta saindo da garagem
                        # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                        if dveicger.get(iveicger, None) == None:
                            dveicger[iveicger] = [sprefvei, iseghini, bsaidgar]
                        else:
                            if iseghini < dveicger[iveicger][1]:
                                dveicger[iveicger] = [sprefvei, iseghini, bsaidgar]
                        # ////////////////////////////////////////////
                        # Definindo as informações que serão impressas
                        # ////////////////////////////////////////////
                        if bsaidgar:                # Saída da garagem
                            scodolin = lauxi001[0]
                            iveicpro = lauxi001[1]
                            stipodia = lauxi001[2]
                            hseghini = abnf_converte_segundos_em_hora_string(iseghini, False)
                            iidveicu = lauxi001[6]
                            iidveofi = lauxi001[8]
                            sdescset = lauxi001[9]  if lauxi001[9]  != None else ''
                            iqtporve = lauxi001[10]
                            bperqtpd = lauxi001[11]
                            bperveca = lauxi001[12]
                            bpervesa = lauxi001[13]
                            inumport = lauxi001[14]
                            barcondi = lauxi001[15]
                            bbprviag = True         # Busca a primeira viagem após saída da garagem
                        elif bbprviag:              # Em 07/08/2025 o Jean falou pediu para pegar a primeira viagem logo após a saída da garagem.
                            bbprviag = False        # Para de buscar a primeira viagem após saída da garagem
                            ssentido = lauxi001[4]
                            sdesolor = lauxi001[5][:30]
                            if   irelator == 2 and sdescset == '': bvalidad = False
                            elif irelator == 3 and sdescset != '': bvalidad = False
                            else: bvalidad = True
                            if bvalidad:
                                if iidveicu == iidveofi:
                                    sauxi001 = '<table border="1"><tr><td><font color=green FACE="Courier New" size=2><b>TIT</b></font></td></tr></table>'
                                else:
                                    sauxi001 = '<table border="1"><tr><td><font color=red FACE="Courier New" size=2><b>SUB</b></font></td></tr></table>'
                                if inumport != None and iqtporve > inumport and bperqtpd == True:       # Quantidade de portas divergente com permissão de divergência
                                    sauxi001 = sauxi001 + '<table border="1"><tr><td bgcolor=yellow><font color=black FACE="Courier New" size=2><b>VEÍCULO COM PORTAS FORA DO PADRÃO!</b></font></td></tr></table>'
                                if inumport != None and iqtporve > inumport and bperqtpd == False:      # Quantidade de portas divergente sem permissão de divergência
                                    sauxi001 = sauxi001 + '<table border="1"><tr><td bgcolor=#E87864><font color=black FACE="Courier New" size=2><b>VEÍCULO COM PORTAS FORA DO PADRÃO!</b></font></td></tr></table>'
                                # Linhas-serviços sem veículos
                                if iidveicu == None:
                                    sauxi002 = '[' +     + '-' + str(iveicpro) + ']'
                                    if not sauxi002 in slinsvei:
                                        slinsvei = slinsvei + sauxi002 + ' ' 
                                abnf_imprime_info_001(sarquwri, None, None, 1,
                                    [
                                        (scodolin, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (iveicpro, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (sprefvei, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (sauxi003, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (sdescset, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                        (sauxi001, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                        (stipodia, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (hseghini, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (ssentido, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                        (sdesolor, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                    ]
                                )
                    # ////////////////////////////
                    # Linhas-serviços sem veículos
                    # ////////////////////////////
                    if slinsvei != '':
                        abnf_imprime_line(sarquwri, icolspan, 'black')
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                ('Linhas-serviços sem veículos:', 4, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                (slinsvei,             icolspan - 4, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
                    # ////////
                    # Externos
                    # ////////
                    sauxi001 = ''
                    lauxi001 = []
                    for lauxi002 in dveicger:
                        if dveicger[lauxi002][2] == False:
                            lauxi001.append(dveicger[lauxi002][0])
                    for sauxi002 in sorted(lauxi001):
                        sauxi001 = sauxi001 + (' - ' if sauxi001 != '' else '') + sauxi002
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    abnf_imprime_info_001(sarquwri, None, None, 1,
                        [
                            ('Externos:',            4, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sauxi001,    icolspan - 4, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                    # ////////////////////////////////////////////////////////////////////////////////////
                    # Buscando veículos que estavam retidos com status 01 e 02 em ddataaux
                    # Apesar de retidos, o veículo só vai entrar na relação se não tiver sido usado no dia
                    # Isso porque a ordem de retenção pode ter sido executada no dia do uso do veículo
                    # ////////////////////////////////////////////////////////////////////////////////////
                    sauxi001 = 'SELECT '
                    # Campos das tabelas
                    sauxi001 = sauxi001 + 'abnf02.prefvei ' # [00] Prefixo do veículo
                    # Tabela de retenção
                    sauxi001 = sauxi001 + 'FROM abnf_operacional_movimentacao_programacao_retencao_veiculos AS abnf01 '
                    # Tabela de veículos
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos                                AS abnf02 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                    # Cláusula WHERE
                    sauxi001 = sauxi001 + 'WHERE '
                    sauxi001 = sauxi001 + 'abnf01.situreg != "C" AND '                  # ==> Somente registros não cancelados (retenção)
                    sauxi001 = sauxi001 + 'abnf01.idfilia = ' + str(iidfilia) + ' AND ' # ==> Somente registros da filial
                    sauxi001 = sauxi001 + 'abnf01.statret IN (1, 2) AND '               # ==> Somente retenções status 01 (preso) e 02 (retido)
                    sauxi001 = sauxi001 + '('
                    sauxi001 = sauxi001 + '(abnf01.dataage <= "' + str(ddataaux) + '" AND abnf01.dtliber >= "' + str(ddataaux) + '") OR '
                    sauxi001 = sauxi001 + '(abnf01.dataage <= "' + str(ddataaux) + '" AND abnf01.dtliber IS NULL)'
                    sauxi001 = sauxi001 + ') '                    
                    # Ordenação
                    sauxi001 = sauxi001 + 'ORDER BY abnf02.prefvei, abnf01.dataage;'
                    # Execução
                    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                    for lauxi001 in lsqlre01:
                        if not lauxi001[0] in lretidos and not lauxi001[0] in lprefvei:
                            lretidos.append(lauxi001[0])
                    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    # Veículos reservas do dia
                    # São todos os veículos do cadastro que não estiverem na lista de usados no dia (lprefvei) e nem na lista de retidos no dia (lretidos)
                    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    if lprefvei == []: lprefvei = [0]
                    if lretidos == []: lretidos = [0]
                    lcamposb = ('prefvei', None)
                    lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '=', 'A'), ('veielev', '!=', True), ('prefvei', '[NotInList]', list(lprefvei)), ('prefvei', '[NotInList]', list(lretidos)))
                    lorderby = ('prefvei', 'idveicu')
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                    sauxi001 = ''
                    for lauxi001 in lsqlre01:
                        sauxi001 = sauxi001 + (' - ' if sauxi001 != '' else '') + lauxi001[0]
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    abnf_imprime_info_001(sarquwri, None, None, 1,
                        [
                            ('Reservas:',            4, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sauxi001,    icolspan - 4, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                    # ////////
                    # Reservas
                    # ////////
                    sauxi001 = ''
                    for lauxi001 in sorted(lretidos):
                        sauxi001 = sauxi001 + (' - ' if sauxi001 != '' else '') + lauxi001
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    abnf_imprime_info_001(sarquwri, None, None, 1,
                        [
                            ('Retidos:',            4, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sauxi001,   icolspan - 4, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                    # ////////////
                    # Próxima data
                    # ////////////
                    ddataaux = abnf_soma_dias_data(ddataaux, 1)
            elif irelator == 4:
                # ////////////////////////////////////////////
                # 04 - SAÍDA DE GARAGEM - VEÍCULOS POR SETORES
                # ////////////////////////////////////////////
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_info_001(sarquwri, '#B1C8C9', 'center', 1,
                    [
                        ('Setor',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Lotação',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Alocados', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Veículos', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_fthead_tbody(sarquwri)
                ddataaux = ddataini                
                while ddataaux <= ddatafim:
                    lprefvei = []   # Lista de veículos usados no dia
                    dveicger = {}   # Dicionário para definir se o veículo geral esta iniciando na garagem (caso não iniciar então ele é EXTERNO)
                    lretidos = []   # Lista de veículos retidos
                    # /////////////////
                    # Cabeçalho por dia
                    # /////////////////
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    abnf_imprime_info_001(sarquwri, '#8EDADE', 'center', 1,
                        [
                            (abnf_converte_data(ddataaux), icolspan, 0, None, None, 'black', 'Courier New', ifontlen + 2, True, False),
                        ]
                    )                    
                    abnf_imprime_info_001(sarquwri, '#B1C8C9', 'center', 1,
                        [
                            ('Setor',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Lotação',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Alocados', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Veículos', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    # ////////////////////////////////////////////
                    # Dados de setores-veiculos da data em análise
                    # ////////////////////////////////////////////
                    sauxi001 = 'SELECT '
                    # Campos das tabelas
                    sauxi001 = sauxi001 + 'abnf03.codoset, '    # [00] Código do setor
                    sauxi001 = sauxi001 + 'abnf03.descset, '    # [01] Descrição do setor
                    sauxi001 = sauxi001 + 'abnf03.qtdveic, '    # [02] Quantidade de veículos
                    sauxi001 = sauxi001 + 'abnf02.prefvei, '    # [03] Prefixo do veículo
                    sauxi001 = sauxi001 + 'abnf01.veicger, '    # [04] Veículo geral
                    sauxi001 = sauxi001 + 'abnf01.seghini, '    # [05] Horário de início (em segundos)
                    sauxi001 = sauxi001 + 'abnf01.saidgar  '    # [06] Saida de garagem?
                    # Tabelas SQL
                    sauxi001 = sauxi001 + 'FROM       abnf_operacional_movimentacao_programacao_diario AS abnf01 '
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_cadastro_veiculos                           AS abnf02 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_operacional_cadastro_setor_veiculos         AS abnf03 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idosetv = abnf03.idosetv '
                    # Condições SQL
                    sauxi001 = sauxi001 + 'WHERE abnf01.situreg != "C" '                    # ==> Somente registros não cancelados (diário)
                    sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                    # ==> Somente registros não cancelados (veículos)
                    sauxi001 = sauxi001 + 'AND   abnf01.idfilia = ' + str(iidfilia) + ' '   # ==> Somente registros da filial
                    sauxi001 = sauxi001 + 'AND   abnf01.dataope = "' + str(ddataaux) + '" ' # ==> Somente registros da data em análise
                    # Ordenação
                    sauxi001 = sauxi001 + 'ORDER BY abnf03.codoset, abnf03.descset, abnf02.prefvei;'
                    # Execução
                    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                    # Debug (início)
                    # abnf_show('05', iqtdre01, 0)
                    # abnf_show('06', lsqlre01, 1)
                    # Debug (fim)
                    dsetnome = {}
                    dsetqtdv = {}
                    dsetveic = {}
                    for lauxi001 in lsqlre01:
                        icodoset = lauxi001[0]
                        sdescset = lauxi001[1]
                        iqtdveic = lauxi001[2]
                        sprefvei = lauxi001[3]
                        iveicger = lauxi001[4]
                        iseghini = lauxi001[5]
                        bsaidgar = lauxi001[6]
                        # ////////////////////////////////////////////////
                        # Abastecendo os dicionários de divisão de setores
                        # ////////////////////////////////////////////////
                        if icodoset != None:
                            if dsetnome.get(icodoset, None) == None:
                                dsetnome[icodoset] = (sdescset, iqtdveic)
                                dsetqtdv[icodoset] = 1
                                dsetveic[icodoset] = sprefvei
                            else:
                                dsetqtdv[icodoset] = dsetqtdv[icodoset] + 1
                                dsetveic[icodoset] = dsetveic[icodoset] + ' - ' + sprefvei
                        # //////////////////////
                        # Abastecendo 'lprefvei'
                        # //////////////////////
                        if sprefvei != '' and not sprefvei in lprefvei:
                            lprefvei.append(sprefvei)
                        # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                        # Abastecendo 'dveicger' com o horário menor de saída que tiver e com a informação se esta saindo da garagem
                        # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                        if dveicger.get(iveicger, None) == None:
                            dveicger[iveicger] = [sprefvei, iseghini, bsaidgar]
                        else:
                            if iseghini < dveicger[iveicger][1]:
                                dveicger[iveicger] = [sprefvei, iseghini, bsaidgar]
                    # ////////////////////
                    # Veículos com setores
                    # ////////////////////
                    for icodoset in dsetnome:
                        abnf_imprime_line(sarquwri, icolspan, 'black')
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                (dsetnome[icodoset][0], 1, 0, None, None,     'black', 'Courier New', ifontlen, True, False),
                                (dsetnome[icodoset][1], 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                (dsetqtdv[icodoset],    1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                (dsetveic[icodoset],    1, 0, None, None,     'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
                    # ////////
                    # Externos
                    # ////////
                    sauxi001 = ''
                    lauxi001 = []
                    for lauxi002 in dveicger:
                        if dveicger[lauxi002][2] == False:
                            lauxi001.append(dveicger[lauxi002][0])
                    for sauxi002 in sorted(lauxi001):
                        sauxi001 = sauxi001 + (' - ' if sauxi001 != '' else '') + sauxi002
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    abnf_imprime_info_001(sarquwri, None, None, 1,
                        [
                            ('Externos:',            1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sauxi001,    icolspan - 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                    # ////////////////////////////////////////////////////////////////////////////////////
                    # Buscando veículos que estavam retidos com status 01 e 02 em ddataaux
                    # Apesar de retidos, o veículo só vai entrar na relação se não tiver sido usado no dia
                    # Isso porque a ordem de retenção pode ter sido executada no dia do uso do veículo
                    # ////////////////////////////////////////////////////////////////////////////////////
                    sauxi001 = 'SELECT '
                    # Campos das tabelas
                    sauxi001 = sauxi001 + 'abnf02.prefvei ' # [00] Prefixo do veículo
                    # Tabela de retenção
                    sauxi001 = sauxi001 + 'FROM abnf_operacional_movimentacao_programacao_retencao_veiculos AS abnf01 '
                    # Tabela de veículos
                    sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos                                AS abnf02 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                    # Cláusula WHERE
                    sauxi001 = sauxi001 + 'WHERE '
                    sauxi001 = sauxi001 + 'abnf01.situreg != "C" AND '                  # ==> Somente registros não cancelados (retenção)
                    sauxi001 = sauxi001 + 'abnf01.idfilia = ' + str(iidfilia) + ' AND ' # ==> Somente registros da filial
                    sauxi001 = sauxi001 + 'abnf01.statret IN (1, 2) AND '               # ==> Somente retenções status 01 (preso) e 02 (retido)
                    sauxi001 = sauxi001 + '('
                    sauxi001 = sauxi001 + '(abnf01.dataage <= "' + str(ddataaux) + '" AND abnf01.dtliber >= "' + str(ddataaux) + '") OR '
                    sauxi001 = sauxi001 + '(abnf01.dataage <= "' + str(ddataaux) + '" AND abnf01.dtliber IS NULL)'
                    sauxi001 = sauxi001 + ') '                    
                    # Ordenação
                    sauxi001 = sauxi001 + 'ORDER BY abnf02.prefvei, abnf01.dataage;'
                    # Execução
                    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                    for lauxi001 in lsqlre01:
                        if not lauxi001[0] in lretidos and not lauxi001[0] in lprefvei:
                            lretidos.append(lauxi001[0])
                    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    # Veículos reservas do dia
                    # São todos os veículos do cadastro que não estiverem na lista de usados no dia (lprefvei) e nem na lista de retidos no dia (lretidos)
                    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    if lprefvei == []: lprefvei = [0]
                    if lretidos == []: lretidos = [0]
                    lcamposb = ('prefvei', None)
                    lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '=', 'A'), ('veielev', '!=', True), ('prefvei', '[NotInList]', list(lprefvei)), ('prefvei', '[NotInList]', list(lretidos)))
                    lorderby = ('prefvei', 'idveicu')
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                    sauxi001 = ''
                    for lauxi001 in lsqlre01:
                        sauxi001 = sauxi001 + (' - ' if sauxi001 != '' else '') + lauxi001[0]
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    abnf_imprime_info_001(sarquwri, None, None, 1,
                        [
                            ('Reservas:',            1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sauxi001,    icolspan - 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                    # ////////
                    # Reservas
                    # ////////
                    sauxi001 = ''
                    for lauxi001 in sorted(lretidos):
                        sauxi001 = sauxi001 + (' - ' if sauxi001 != '' else '') + lauxi001
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    abnf_imprime_info_001(sarquwri, None, None, 1,
                        [
                            ('Retidos:',            1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sauxi001,   icolspan - 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                    # ////////////
                    # Próxima data
                    # ////////////
                    ddataaux = abnf_soma_dias_data(ddataaux, 1)
            elif irelator == 5:
                # ////////////////////////////////////////////
                # 05 - SAÍDA DE GARAGEM - SETORES POR VEÍCULOS
                # ////////////////////////////////////////////
                # ////////////////////////////////////////////////////////////////////////////////////////////////////////
                # Criando o dicionário e a lista de todos os veículos ativos da frota (com exceção dos veículos do Elevar)
                # ////////////////////////////////////////////////////////////////////////////////////////////////////////
                didveicu = {}
                lidveicu = []
                lcamposb = ('idveicu', 'prefvei')
                lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '=', 'A'), ('veielev', '!=', True))
                lorderby = ('prefvei', 'idveicu')
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                sauxi001 = ''
                for lauxi001 in lsqlre01:
                    didveicu[lauxi001[0]] = None
                    lidveicu.append([lauxi001[1], lauxi001[0], None])
                # ////////////////////////////////////////////////////////
                # Definindo os quadrantes de cada um dos veiculos da lista
                # ////////////////////////////////////////////////////////
                lauxi001 = [0, 0, 0, 0, 0]  # <= Quadrantes de veiculos
                iquadran = len(lauxi001)
                icontd01 = 0
                icontd02 = 0
                while icontd01 < len(lidveicu):
                    lauxi001[icontd02] = lauxi001[icontd02] + 1
                    icontd01 += 1
                    icontd02 += 1
                    if icontd02 > 4:
                        icontd02 = 0
                for lauxi002 in lidveicu:
                    for icontd01 in range(iquadran):
                        if lauxi001[icontd01] > 0:
                            lauxi001[icontd01] = lauxi001[icontd01] - 1
                            lauxi002[2] = icontd01
                            break
                # Debug (início)
                # abnf_show('07', lauxi001, 1)
                # abnf_show('08', len(lidveicu), 0)
                # abnf_show('09', lidveicu, 1)
                # abnf_show('10', didveicu, 2)
                # Debug (fim)
                abnf_imprime_fthead_tbody(sarquwri)
                ddataaux = ddataini
                while ddataaux <= ddatafim:
                    dveicger = {}   # Dicionário para definir se o veículo geral esta iniciando na garagem (caso não iniciar então ele é EXTERNO)
                    # ////////////////////////////////////////////
                    # Dados de setores-veiculos da data em análise
                    # ////////////////////////////////////////////
                    sauxi001 = 'SELECT '
                    # Campos das tabelas
                    sauxi001 = sauxi001 + 'abnf03.codoset, '    # [00] Código do setor
                    sauxi001 = sauxi001 + 'abnf03.descset, '    # [01] Descrição do setor
                    sauxi001 = sauxi001 + 'abnf02.idveicu, '    # [02] ID do veículo
                    sauxi001 = sauxi001 + 'abnf01.veicger, '    # [03] Veículo geral
                    sauxi001 = sauxi001 + 'abnf01.seghini, '    # [04] Horário de início (em segundos)
                    sauxi001 = sauxi001 + 'abnf01.saidgar  '    # [05] Saida de garagem?
                    # Tabelas SQL
                    sauxi001 = sauxi001 + 'FROM       abnf_operacional_movimentacao_programacao_diario AS abnf01 '
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_cadastro_veiculos                           AS abnf02 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                    sauxi001 = sauxi001 + 'LEFT JOIN  abnf_operacional_cadastro_setor_veiculos         AS abnf03 '
                    sauxi001 = sauxi001 + 'ON         abnf01.idosetv = abnf03.idosetv '
                    # Condições SQL
                    sauxi001 = sauxi001 + 'WHERE abnf01.situreg != "C" '                    # ==> Somente registros não cancelados (diário)
                    sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                    # ==> Somente registros não cancelados (veículos)
                    sauxi001 = sauxi001 + 'AND   abnf01.idfilia = ' + str(iidfilia) + ' '   # ==> Somente registros da filial
                    sauxi001 = sauxi001 + 'AND   abnf01.dataope = "' + str(ddataaux) + '" ' # ==> Somente registros da data em análise
                    # Ordenação
                    sauxi001 = sauxi001 + 'ORDER BY abnf03.codoset, abnf03.descset, abnf02.prefvei;'
                    # Execução
                    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                    # Debug (início)
                    # abnf_show('05', iqtdre01, 0)
                    # abnf_show('06', lsqlre01, 1)
                    # Debug (fim)
                    if lsqlre01 != [] and iqtdre01 > 0:
                        # ///////////////////////////////
                        # Limpando os dados do dicionário
                        # ///////////////////////////////
                        for lauxi002 in didveicu:
                            didveicu[lauxi002] = None
                        # ///////////////////////
                        # Abastecendo os veículos
                        # ///////////////////////
                        for lauxi001 in lsqlre01:
                            icodoset = lauxi001[0]
                            sdescset = lauxi001[1]
                            iidveicu = lauxi001[2]
                            iveicger = lauxi001[3]
                            iseghini = lauxi001[4]
                            bsaidgar = lauxi001[5]
                            # ////////////////////////////////////////////////////
                            # Abastecendo os dicionários com informação de setores
                            # ////////////////////////////////////////////////////
                            if icodoset != None:
                                didveicu[iidveicu] = sdescset
                            else:
                                didveicu[iidveicu] = 'Op.Parcial'
                            # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                            # Abastecendo 'dveicger' com o horário menor de saída que tiver e com a informação se esta saindo da garagem
                            # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                            if dveicger.get(iveicger, None) == None:
                                dveicger[iveicger] = [iidveicu, iseghini, bsaidgar]
                            else:
                                if iseghini < dveicger[iveicger][1]:
                                    dveicger[iveicger] = [iidveicu, iseghini, bsaidgar]
                        # ////////
                        # Externos
                        # ////////
                        for lauxi001 in dveicger:
                            if dveicger[lauxi001][2] == False:
                                didveicu[dveicger[lauxi001][0]] = 'Externo'
                        # ////////////////////////////////////////////////////////////////////////////////////
                        # Buscando veículos que estavam retidos com status 01 e 02 em ddataaux
                        # Apesar de retidos, o veículo só vai entrar na relação se não tiver sido usado no dia
                        # Isso porque a ordem de retenção pode ter sido executada no dia do uso do veículo
                        # ////////////////////////////////////////////////////////////////////////////////////
                        sauxi001 = 'SELECT '
                        # Campos das tabelas
                        sauxi001 = sauxi001 + 'abnf02.idveicu ' # [00] ID do veículo
                        # Tabela de retenção
                        sauxi001 = sauxi001 + 'FROM abnf_operacional_movimentacao_programacao_retencao_veiculos AS abnf01 '
                        # Tabela de veículos
                        sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos                                AS abnf02 '
                        sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                        # Cláusula WHERE
                        sauxi001 = sauxi001 + 'WHERE abnf01.situreg != "C" '                    # ==> Somente registros não cancelados (retenção)
                        sauxi001 = sauxi001 + 'AND   abnf01.idfilia = ' + str(iidfilia) + ' '   # ==> Somente registros da filial
                        sauxi001 = sauxi001 + 'AND   abnf01.statret IN (1, 2) '                 # ==> Somente retenções status 01 (preso) e 02 (retido)
                        sauxi001 = sauxi001 + 'AND   abnf02.veielev = False '                   # ==> Somente veículos que não são do Elevar
                        sauxi001 = sauxi001 + 'AND ('
                        sauxi001 = sauxi001 + '(abnf01.dataage <= "' + str(ddataaux) + '" AND abnf01.dtliber >= "' + str(ddataaux) + '") OR '
                        sauxi001 = sauxi001 + '(abnf01.dataage <= "' + str(ddataaux) + '" AND abnf01.dtliber IS NULL)'
                        sauxi001 = sauxi001 + ') '                    
                        # Ordenação
                        sauxi001 = sauxi001 + 'ORDER BY abnf02.idveicu, abnf01.dataage;'
                        # Execução
                        lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                        # Debug (início)
                        # abnf_show('09', didveicu, 2)
                        # abnf_show('10', lsqlre01, 1)
                        # abnf_show('09', lidveicu, 1)
                        # abnf_show('10', didveicu, 2)
                        # Debug (fim)
                        for lauxi001 in lsqlre01:
                            # Debug (início)
                            # abnf_show('05', lauxi001, 0)
                            # abnf_show('06', lauxi001[0], 0)
                            # abnf_show('07', didveicu[lauxi001[0]], 0)
                            # Debug (fim)
                            if didveicu[lauxi001[0]] == None:
                                didveicu[lauxi001[0]] = 'Retido'
                        # ////////////////////////////////////////////////////////////////
                        # Reservas (todos ítens de "didveicu" que tiverem com valor "None"
                        # ////////////////////////////////////////////////////////////////
                        for iidveicu in didveicu:
                            if didveicu[iidveicu] == None:
                                didveicu[iidveicu] = 'Reserva'
                        # ///////////////////////////////////
                        # Montando os quadrantes do relatório
                        # ///////////////////////////////////
                        sauxi001 = '<table border="3">'
                        sauxi001 = sauxi001 + '   <tr><td colspan="5" bgcolor="darkcyan"></td></tr>'
                        sauxi001 = sauxi001 + '   <tr bgcolor="#8EDADE" align="center">'
                        sauxi001 = sauxi001 + '       <td colspan="5"><font color=black FACE="Courier New" size=4><b>' + abnf_converte_data(ddataaux) + '</b></font></td>'
                        sauxi001 = sauxi001 + '   </tr>'
                        sauxi001 = sauxi001 + '   <tr><td colspan="5" bgcolor="darkcyan"></td></tr>'
                        sauxi001 = sauxi001 + '   <tr valign="top" bgcolor=#808080>' + '\n'
                        for icontd01 in range(iquadran):
                            sauxi001 = sauxi001 + '      <td><table border="2">'  + '\n'
                            sauxi001 = sauxi001 + '             <tr bgcolor=#A9B3DB>' + '\n'
                            sauxi001 = sauxi001 + '                <td align="center"><font color=black FACE="Courier New" size=3><b>VEICULO</b></font></td>' + '\n'
                            sauxi001 = sauxi001 + '                <td align="center"><font color=black FACE="Courier New" size=3><b>LOCAL</b></font></td>' + '\n'
                            sauxi001 = sauxi001 + '             </tr>'  + '\n'
                            for lauxi001 in lidveicu:
                                if lauxi001[2] == icontd01:
                                    sauxi001 = sauxi001 + '         <tr bgcolor=white>' + '\n'
                                    sauxi001 = sauxi001 + '            <td align="center"><font color=black FACE="Courier New" size=2><b>' + lauxi001[0] + '</b></font></td>'  + '\n'
                                    sauxi001 = sauxi001 + '            <td><font color=black FACE="Courier New" size=2><b>' + str(didveicu[lauxi001[1]]) + '</b></font></td>'  + '\n'
                                    sauxi001 = sauxi001 + '         </tr>'  + '\n'
                            sauxi001 = sauxi001 + '      </table></td>'  + '\n'
                        sauxi001 = sauxi001 + '   </tr>' + '\n'
                        sauxi001 = sauxi001 + '</table>'
                        sarquwri.write(sauxi001 + '\n')
                    ddataaux = abnf_soma_dias_data(ddataaux, 1)
            elif irelator in (6, 7):
                # /////////////////////////////
                # 06 - DIÁRIO POR LINHA-SERVIÇO
                # 07 - DIÁRIO POR VEÍCULO
                # /////////////////////////////
                abnf_imprime_line(sarquwri, icolspan, 'black')
                if irelator == 6:
                    lauxi001 = [
                        ('Linha',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Serviço',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Veículo',  2, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ]
                elif irelator == 7:
                    lauxi001 = [
                        ('Veículo',  2, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Linha',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Serviço',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ]
                lauxi001 = lauxi001 + [
                    ('Tipo dia', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Partida',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Sentido',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Origem',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Destino',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('TV',       1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
                abnf_imprime_info_001(sarquwri, '#B1C8C9', 'center', 1, lauxi001)
                # abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_fthead_tbody(sarquwri)
                # ////////////////////////
                # Dados de linhas-serviços
                # ////////////////////////
                sauxi001 = 'SELECT '
                # Campos das tabelas
                sauxi001 = sauxi001 + 'abnf01.codolin, '    # [00] Codigo da linha
                sauxi001 = sauxi001 + 'abnf02.veicpro, '    # [01] Veículo-Serviço
                sauxi001 = sauxi001 + 'abnf02.idveicu, '    # [02] ID do veículo
                sauxi001 = sauxi001 + 'abnf05.prefvei, '    # [03] Prefixo do veículo
                sauxi001 = sauxi001 + 'abnf02.idveofi, '    # [04] ID do veículo oficial
                sauxi001 = sauxi001 + 'abnf02.tipodia, '    # [05] Tipo de dia
                sauxi001 = sauxi001 + 'abnf02.seghini, '    # [06] Horário de início (em segundos)
                sauxi001 = sauxi001 + 'abnf02.sentido, '    # [07] Sentido
                sauxi001 = sauxi001 + 'abnf03.desoloc, '    # [08] Descrição do local de origem
                sauxi001 = sauxi001 + 'abnf04.desoloc, '    # [09] Descrição do local de destino
                sauxi001 = sauxi001 + 'abnf02.idotivi  '    # [10] Tipo de viagem: 1=Ocioso/2=Produtivo/3=Reservado/4=Deslocamento
                # Tabelas SQL
                sauxi001 = sauxi001 + 'FROM       abnf_operacional_cadastro_linhas                 AS abnf01 '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_programacao_diario AS abnf02 '
                sauxi001 = sauxi001 + 'ON         abnf01.idolinh = abnf02.idolinh '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_locais                 AS abnf03 '
                sauxi001 = sauxi001 + 'ON         abnf02.idolori = abnf03.idoloca '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_locais                 AS abnf04 '
                sauxi001 = sauxi001 + 'ON         abnf02.idoldes = abnf04.idoloca '
                sauxi001 = sauxi001 + 'LEFT JOIN  abnf_cadastro_veiculos                           AS abnf05 '
                sauxi001 = sauxi001 + 'ON         abnf02.idveicu = abnf05.idveicu '
                # Condições SQL
                sauxi001 = sauxi001 + 'WHERE abnf01.situreg != "C" '                    # ==> Somente registros não cancelados (linhas)
                sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                    # ==> Somente registros não cancelados (diário)
                sauxi001 = sauxi001 + 'AND   abnf02.idfilia = ' + str(iidfilia) + ' '   # ==> Somente registros da filial
                sauxi001 = sauxi001 + 'AND   abnf02.dataope = "' + str(ddataini) + '" ' # ==> Somente registros da data em análise
                # Ordenação
                if   irelator == 6: sauxi001 = sauxi001 + 'ORDER BY abnf01.codolin, abnf02.veicpro, abnf02.seghini;'
                elif irelator == 7: sauxi001 = sauxi001 + 'ORDER BY abnf05.prefvei, abnf02.seghini;'
                # Execução
                lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                # Debug (início)
                # abnf_show('05', lsqlre01, 1)
                # Debug (fim)
                lauxi002 = ['', 0]
                sauxi002 = ''
                for lauxi001 in lsqlre01:
                    icontreg += 1
                    scodolin = lauxi001[0]
                    iveicpro = lauxi001[1]
                    iidveicu = lauxi001[2]
                    sprefvei = lauxi001[3] if lauxi001[3] != None else '[SEM&nbsp;VEÍCULO]'
                    iidveofi = lauxi001[4]
                    stipodia = abnf_personal_retorna_string(13001,lauxi001[5])
                    hseghini = abnf_converte_segundos_em_hora_string(lauxi001[6], False)
                    ssentido = abnf_personal_retorna_string(10131, lauxi001[7])
                    sdesolor = lauxi001[8]
                    sdesolde = lauxi001[9]
                    sidotivi = abnf_personal_retorna_string(10133, lauxi001[10])
                    if   iidveicu == None:     sauxi001, sfontcol = (''   , 'black')
                    elif iidveicu == iidveofi: sauxi001, sfontcol = ('TIT', 'green')
                    else:                      sauxi001, sfontcol = ('SUB', 'red')
                    if irelator == 6:
                        if [scodolin, iveicpro] != lauxi002:
                            abnf_imprime_line(sarquwri, icolspan, 'black')
                            lauxi002 = [scodolin, iveicpro]
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                (scodolin, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (iveicpro, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (sprefvei, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (sauxi001, 1, 0, None, 'center', sfontcol, 'Courier New', ifontlen, True, False),
                                (stipodia, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (hseghini, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (ssentido, 1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                                (sdesolor, 1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                                (sdesolde, 1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                                (sidotivi, 1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                            ]
                        )  
                    elif irelator == 7:
                        if sprefvei != sauxi002:
                            abnf_imprime_line(sarquwri, icolspan, 'black')
                            sauxi002 = sprefvei
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                (sprefvei, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (sauxi001, 1, 0, None, 'center', sfontcol, 'Courier New', ifontlen, True, False),
                                (scodolin, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (iveicpro, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (stipodia, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (hseghini, 1, 0, None, 'center', 'black',  'Courier New', ifontlen, True, False),
                                (ssentido, 1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                                (sdesolor, 1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                                (sdesolde, 1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                                (sidotivi, 1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                            ]
                        )
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        ('Total de viagens impressas:', icolspan - 1, 0, None, 'Left'  , 'black', 'Courier New', ifontlen, True, False),
                        (icontreg,                                 1, 0, None, 'Right' , 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
            elif irelator == 8:
                # //////////////////////////
                # 08 - VEÍCULOS SUBSTITUÍDOS
                # //////////////////////////
                # MariaDB [gb001]> SELECT * FROM abnf_operacional_movimentacao_programacao_substituicao;
                # +---------+---------+---------+---------+---------+-----------+---------+---------+---------+---------------------+---------+
                # | idoprsu | idoprdi | tiposub | idveisa | idveien | observa   | situreg | idusucr | idusual | dtregcr             | dtregal |
                # +---------+---------+---------+---------+---------+-----------+---------+---------+---------+---------------------+---------+
                # |       1 |   31131 | V       |     607 |     629 | TESTE 123 | A       |       2 |    NULL | 2025-08-14 14:30:28 | NULL    |
                # +---------+---------+---------+---------+---------+-----------+---------+---------+---------+---------------------+---------+
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_info_001(sarquwri, '#B1C8C9', 'center', 1,
                    [
                        ('Data operação',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Linha',            1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Serviço',          1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Tipo dia',         1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Partida',          1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Sentido',          1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Origem',           1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Veículos saída',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Veículos entrada', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Motivo',           1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Complemento',      1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Registro',         1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_fthead_tbody(sarquwri)
                # ///////////////////////////////////////////////
                # Filtrando registros de substituição de veículos
                # ///////////////////////////////////////////////
                sauxi001 = 'SELECT '
                # Campos das tabelas
                sauxi001 = sauxi001 + 'abnf02.dataope, '        # [00] Data da operação
                sauxi001 = sauxi001 + 'abnf01.codolin, '        # [01] Codigo da linha
                sauxi001 = sauxi001 + 'abnf02.veicpro, '        # [02] Veículo-Serviço
                sauxi001 = sauxi001 + 'abnf02.tipodia, '        # [03] Tipo de dia
                sauxi001 = sauxi001 + 'abnf02.seghini, '        # [04] Horário de início (em segundos)
                sauxi001 = sauxi001 + 'abnf02.sentido, '        # [05] Sentido
                sauxi001 = sauxi001 + 'abnf04.desoloc, '        # [06] Descrição do local de origem
                sauxi001 = sauxi001 + 'abnf05.prefvei, '        # [07] Prefixo do veículo de saída
                sauxi001 = sauxi001 + 'abnf06.prefvei, '        # [08] Prefixo do veículo de entrada
                sauxi001 = sauxi001 + 'abnf07.descmsu, '        # [09] Motivo da substituição
                sauxi001 = sauxi001 + 'abnf03.motisub, '        # [10] Complemento
                sauxi001 = sauxi001 + 'abnf03.idoprsu  '        # [11] Registro da substituição
                # Tabelas SQL
                sauxi001 = sauxi001 + 'FROM       abnf_operacional_cadastro_linhas                          AS abnf01 '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_programacao_diario          AS abnf02 '
                sauxi001 = sauxi001 + 'ON         abnf01.idolinh = abnf02.idolinh '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_movimentacao_programacao_substituicao    AS abnf03 '
                sauxi001 = sauxi001 + 'ON         abnf02.idoprdi = abnf03.idoprdi '
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_locais                          AS abnf04 '
                sauxi001 = sauxi001 + 'ON         abnf02.idolori = abnf04.idoloca '
                sauxi001 = sauxi001 + 'LEFT JOIN  abnf_cadastro_veiculos                                    AS abnf05 '
                sauxi001 = sauxi001 + 'ON         abnf03.idveisa = abnf05.idveicu '
                sauxi001 = sauxi001 + 'AND        abnf05.situreg != "C" '                                           # ==> Somente registros não cancelados (veículos)
                sauxi001 = sauxi001 + 'LEFT JOIN  abnf_cadastro_veiculos                                    AS abnf06 '
                sauxi001 = sauxi001 + 'ON         abnf03.idveien = abnf06.idveicu '
                sauxi001 = sauxi001 + 'AND        abnf06.situreg != "C" '                                           # ==> Somente registros não cancelados (veículos)
                sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_motivo_substituicao             AS abnf07 '
                sauxi001 = sauxi001 + 'ON         abnf07.idomsub = abnf03.idomsub '
                # Condições SQL
                sauxi001 = sauxi001 + 'WHERE dataope BETWEEN "' + str(ddataini) + '" AND "' + str(ddatafim) + '" '  # ==> Somente registros com data de eoperação dentro do período
                sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                                                # ==> Somente registros não cancelados (diário)
                sauxi001 = sauxi001 + 'AND   abnf03.situreg != "C" '                                                # ==> Somente registros não cancelados (substituição)
                sauxi001 = sauxi001 + 'AND   abnf02.idfilia = ' + str(iidfilia) + ' '                               # ==> Somente registros da filial
                sauxi001 = sauxi001 + 'AND   abnf03.tiposub = "V" '                                                 # ==> Somente registros de substituição de veículos
                # Ordenação
                sauxi001 = sauxi001 + 'ORDER BY abnf02.dataope, abnf02.seghini, abnf03.dtregcr;'
                # Execução
                lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                # Debug (início)
                # abnf_show('05', lsqlre01, 1)
                # Debug (fim)
                for lauxi001 in lsqlre01:
                    sdataope = abnf_converte_data(lauxi001[0])
                    scodolin = lauxi001[1]
                    iveicpro = lauxi001[2]
                    stipodia = abnf_personal_retorna_string(13001,lauxi001[3])
                    hseghini = abnf_converte_segundos_em_hora_string(lauxi001[4], False)
                    ssentido = abnf_personal_retorna_string(10131, lauxi001[5])
                    sdesolor = lauxi001[6]
                    sprefvsa = lauxi001[7] if lauxi001[7] != None else ''
                    sprefven = lauxi001[8] if lauxi001[8] != None else ''
                    sdescmsu = lauxi001[9]
                    smotisub = lauxi001[10]
                    sidoprsu = str(1000000 + lauxi001[11])[1:]
                    abnf_imprime_info_001(sarquwri, None, None, 1,
                        [
                            (sdataope, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (scodolin, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (iveicpro, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (stipodia, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (hseghini, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (ssentido, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sdesolor, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sprefvsa, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (sprefven, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (sdescmsu, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (smotisub, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sidoprsu, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
            elif irelator == 9:
                # ///////////////////////////////////////////////
                # 09 - VEÍCULOS NÃO UTILIZADOS E VEÍCULOS RETIDOS
                # ///////////////////////////////////////////////
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_info_001(sarquwri, '#B1C8C9', 'center', 1,
                    [
                        ('Data',                        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Veículo não utilizados',      1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Veículo retidos (status 01)', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
                abnf_imprime_line(sarquwri, icolspan, 'black')
                # ///////////////////////////////////
                # Dados de linhas-serviços do período
                # ///////////////////////////////////
                sauxi001 = 'SELECT '
                # Campos das tabelas
                sauxi001 = sauxi001 + 'abnf01.dataope, '    # [00] Data da operação
                sauxi001 = sauxi001 + 'abnf02.idveicu, '    # [01] ID do veículo
                sauxi001 = sauxi001 + 'abnf02.prefvei  '    # [02] Prefixo do veículo
                # Tabelas SQL
                sauxi001 = sauxi001 + 'FROM  '
                # Subconsulta para obter as datas únicas no período desejado
                sauxi001 = sauxi001 + '(SELECT DISTINCT dataope, idveicu FROM abnf_operacional_movimentacao_programacao_diario '
                sauxi001 = sauxi001 + 'WHERE dataope BETWEEN "' + str(ddataini) + '" AND "' + str(ddatafim) + '" '
                sauxi001 = sauxi001 + 'AND situreg != "C" AND idfilia = ' + str(iidfilia) + ')                          AS abnf01 '   
                # Tabela de veículos para obter todos os veículos
                sauxi001 = sauxi001 + 'CROSS JOIN '
                sauxi001 = sauxi001 + '(SELECT idveicu, prefvei FROM abnf_cadastro_veiculos '
                # 19/08/2025 - Linha abaixo foi substituida porque Jean pediu para não aparecer carros vendidos.
                # sauxi001 = sauxi001 + 'WHERE situreg != "C" AND idfilia = ' + str(iidfilia) + ' AND veielev != TRUE)  AS abnf02 '
                sauxi001 = sauxi001 + 'WHERE situreg = "A" AND idfilia = ' + str(iidfilia) + ' AND veielev != TRUE)     AS abnf02 '  
                # Tabela de movimentação para verificar o uso
                sauxi001 = sauxi001 + 'LEFT JOIN  abnf_operacional_movimentacao_programacao_diario                      AS abnf03 '
                sauxi001 = sauxi001 + 'ON         abnf01.dataope = abnf03.dataope '
                sauxi001 = sauxi001 + 'AND        abnf02.idveicu = abnf03.idveicu '
                sauxi001 = sauxi001 + 'AND        abnf03.situreg != "C" '                   # ==> Somente registros não cancelados (veículos)
                sauxi001 = sauxi001 + 'AND        abnf03.idfilia = ' + str(iidfilia) + ' '  # ==> Somente registros da filial
                # Filtra apenas os registros onde não houve uso do veículo
                sauxi001 = sauxi001 + 'WHERE abnf03.idoprdi IS NULL '
                # Agrupa por data e prefixo do veículo para evitar duplicatas
                sauxi001 = sauxi001 + 'GROUP BY abnf01.dataope, abnf02.prefvei '
                # Ordenação
                sauxi001 = sauxi001 + 'ORDER BY abnf01.dataope, abnf02.prefvei;'
                # Execução
                lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                ldataope = []
                for lauxi001 in lsqlre01:
                    if not lauxi001[0] in ldataope:
                        ldataope.append(lauxi001[0])
                # //////////////////////////////////////////////////////
                # Filtrando registros de renteção de veículos do período
                # //////////////////////////////////////////////////////
                sauxi001 = 'SELECT '
                # Campos das tabelas
                sauxi001 = sauxi001 + 'abnf01.dataage, '    # [00] Data da retenção
                sauxi001 = sauxi001 + 'abnf01.dtliber, '    # [01] Data da liberação
                sauxi001 = sauxi001 + 'abnf01.idveicu, '    # [02] ID do veículo
                sauxi001 = sauxi001 + 'abnf02.prefvei, '    # [03] Prefixo do veículo
                sauxi001 = sauxi001 + 'abnf01.descrre  '    # [04] Motivo da retenção
                # Tabela de retenção
                sauxi001 = sauxi001 + 'FROM abnf_operacional_movimentacao_programacao_retencao_veiculos AS abnf01 '
                # Tabela de veículos
                sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos                                AS abnf02 '
                sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                # Cláusula WHERE
                sauxi001 = sauxi001 + 'WHERE '
                sauxi001 = sauxi001 + 'abnf01.situreg != "C" AND '                  # ==> Somente registros não cancelados (retenção)
                sauxi001 = sauxi001 + 'abnf01.idfilia = ' + str(iidfilia) + ' AND ' # ==> Somente registros da filial
                sauxi001 = sauxi001 + 'abnf01.statret IN (1, 2) AND '               # ==> Somente retenções status 01 (preso) e 02 (retido)
                sauxi001 = sauxi001 + '((abnf01.dataage      BETWEEN "' + str(ddataini) + '" AND "' + str(ddatafim) + '") OR '
                sauxi001 = sauxi001 + '(DATE(abnf01.dtliber) BETWEEN "' + str(ddataini) + '" AND "' + str(ddatafim) + '") OR '
                sauxi001 = sauxi001 + '(abnf01.dataage < "' + str(ddataini) + '" AND abnf01.dtliber IS NULL)) '
                # Ordenação
                sauxi001 = sauxi001 + 'ORDER BY abnf02.prefvei, abnf01.dataage;'
                # Execução
                lsqlre02, iqtdre02 = abnf_database_executa_sql(icodbase, sauxi001)
                # //////////////////
                # Mostrando os dados
                # //////////////////
                # Debug (início)
                # abnf_show('05', sauxi001, 0)
                # abnf_show('06', lsqlre01, 1)
                # abnf_show('07', lsqlre02, 1)
                # abnf_show('08', ldataope, 1)
                # Debug (fim)
                for ddataope in ldataope:
                    # //////////////////////////
                    # Veículo retidos no período
                    # //////////////////////////
                    sauxi002 = ''
                    lidveicu = []
                    for lauxi001 in lsqlre02:
                        ddataage = lauxi001[0]
                        ddtliber = datetime.date(lauxi001[1]) if lauxi001[1] != None else None
                        if ((ddataope >= ddataage and ddtliber != None and ddataope <= ddtliber) or
                            (ddataope >= ddataage and ddtliber == None)):
                            iidveicu = lauxi001[2]
                            sprefvei = lauxi001[3]
                            sdescrre = lauxi001[4]
                            if sauxi002 == '': sauxi002 = sprefvei
                            else: sauxi002 = sauxi002 + '<br>' + sprefvei + ' - ' + sdescrre
                            lidveicu.append(iidveicu)
                    # /////////////////////////////////////////////////////////
                    # Veículo não utilizados e que não estão retidos no período
                    # /////////////////////////////////////////////////////////
                    sauxi001 = ''
                    for lauxi001 in lsqlre01:
                        ddataaux = lauxi001[0]
                        if ddataaux == ddataope:
                            iidveicu = lauxi001[1]
                            if not iidveicu in lidveicu:
                                sprefvei = lauxi001[2]
                                if sauxi001 == '': sauxi001 = sprefvei
                                else: sauxi001 = sauxi001 + '<br>' + sprefvei
                    # /////////////////////
                    # Mostrar os resultados
                    # /////////////////////
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    abnf_imprime_info_001(sarquwri, None, None, 1,
                        [
                            (abnf_converte_data(ddataope), 1, 0, None, 'center', 'black',  'Courier New', ifontlen + 2, True, False),
                            (sauxi001,                     1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                            (sauxi002,                     1, 0, None, 'left',   'black',  'Courier New', ifontlen, True, False),
                        ]
                    )
            elif irelator == 10:
                # /////////////////////////////////////
                # 10 - RETENÇÃO E LIBERAÇÃO DE VEÍCULOS
                # /////////////////////////////////////
                # ==> ddatafim = abnf_soma_dias_data(ddatafim, 1)
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_info_001(sarquwri, '#B1C8C9', 'center', 1,
                    [
                        ('Agendamento', 3, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Veículo',     1, 2, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Retenção',    7, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Liberação',   3, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ]
                )                
                abnf_imprime_info_001(sarquwri, '#B1C8C9', 'center', 1,
                    [
                        ('Data',        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Hora',        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Controle',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Data/hora',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Motivo',      1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Status',      1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('GSD',         3, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Usuário',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Data/hora',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Observação',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ('Usuário',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_fthead_tbody(sarquwri)
                # //////////////////////////////////////////////////////
                # Filtrando registros de renteção de veículos do período
                # //////////////////////////////////////////////////////
                sauxi001 = 'SELECT '
                # Campos das tabelas
                sauxi001 = sauxi001 + 'abnf01.dataage, '    # [00] Data do agendamento
                sauxi001 = sauxi001 + 'abnf01.seghage, '    # [01] Hora do agendamento
                sauxi001 = sauxi001 + 'abnf01.codctrl, '    # [02] Código de controle
                sauxi001 = sauxi001 + 'abnf02.prefvei, '    # [03] Prefixo do veículo
                sauxi001 = sauxi001 + 'abnf01.dtreten, '    # [04] Data/hora da retenção
                sauxi001 = sauxi001 + 'abnf01.descrre, '    # [05] Motivo da retenção
                sauxi001 = sauxi001 + 'abnf01.statret, '    # [06] Status da retenção
                sauxi001 = sauxi001 + 'abnf07.dessdeg, '    # [07] Descricao do grupo de GSD
                sauxi001 = sauxi001 + 'abnf06.dessdes, '    # [08] Descrição do subgrupo de GSD
                sauxi001 = sauxi001 + 'abnf05.dessded, '    # [09] Descrição da definição de GSD
                sauxi001 = sauxi001 + 'abnf03.nomeusu, '    # [10] Usuário que realizou a retenção
                sauxi001 = sauxi001 + 'abnf01.dtliber, '    # [11] Data/hora da liberação
                sauxi001 = sauxi001 + 'abnf01.descrli, '    # [12] Observação na liberação
                sauxi001 = sauxi001 + 'abnf01.idcusli, '    # [13] Usuário que realizou a liberação
                sauxi001 = sauxi001 + 'abnf04.nomeusu  '    # [14] Usuário que realizou a liberação
                # Tabela de retenção
                sauxi001 = sauxi001 + 'FROM abnf_operacional_movimentacao_programacao_retencao_veiculos AS abnf01 '
                # Tabela de veículos
                sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos                                AS abnf02 '
                sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                # Tabela de usuário (usuário que reteve)
                sauxi001 = sauxi001 + 'INNER JOIN abnf_sistema_usuarios                                 AS abnf03 '
                sauxi001 = sauxi001 + 'ON         abnf01.idcusre = abnf03.idusuar '
                # Tabela de usuário (usuário que liberou)
                sauxi001 = sauxi001 + 'LEFT JOIN abnf_sistema_usuarios                                  AS abnf04 '
                sauxi001 = sauxi001 + 'ON        abnf01.idcusli = abnf04.idusuar '
                # Tabela definição de GSD
                sauxi001 = sauxi001 + 'LEFT JOIN abnf_sigom_cadastro_defeitos_definicoes                AS abnf05 '
                sauxi001 = sauxi001 + 'ON        abnf01.idsdede = abnf05.idsdede '
                # Tabela de subgrupos de GSD
                sauxi001 = sauxi001 + 'LEFT JOIN abnf_sigom_cadastro_defeitos_subgrupos                 AS abnf06 '
                sauxi001 = sauxi001 + 'ON        abnf05.idsdesg = abnf06.idsdesg '
                # Tabela de grupo de GSD
                sauxi001 = sauxi001 + 'LEFT JOIN abnf_sigom_cadastro_defeitos_grupos                    AS abnf07 '
                sauxi001 = sauxi001 + 'ON        abnf06.idsdegr = abnf07.idsdegr '
                # Cláusula WHERE
                sauxi001 = sauxi001 + 'WHERE '
                sauxi001 = sauxi001 + 'abnf01.idfilia = ' + str(iidfilia) + ' AND ' # ==> Somente registros da filial
                sauxi001 = sauxi001 + 'abnf01.situreg != "C" AND '                  # ==> Somente registros não cancelados (retenção)
                sauxi001 = sauxi001 + 'abnf01.dataage BETWEEN "' + str(ddataini) + '" AND "' + str(ddatafim) + '" '
                # Ordenação
                # (28/08/2025 - Alterado a busca pela data do agendamento # sauxi001) sauxi001 = sauxi001 + 'ORDER BY abnf01.dtreten, abnf02.prefvei;'
                sauxi001 = sauxi001 + 'ORDER BY abnf01.dataage, abnf01.seghage, abnf02.prefvei;'
                # Execução
                lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                # Debug (início)
                # abnf_show('05', lsqlre01, 1)
                # Debug (fim)
                for lauxi001 in lsqlre01:
                    icontreg += 1
                    sdataage = abnf_converte_data(lauxi001[0])
                    hseghage = abnf_converte_segundos_em_hora_string(lauxi001[1], False)
                    scodctrl = str(1000000 + lauxi001[2])[1:]
                    sprefvei = lauxi001[3]
                    sdtreten = abnf_converte_datahora(lauxi001[4], 1)
                    sdescrre = lauxi001[5]
                    sstatret = abnf_personal_retorna_string(13002, lauxi001[6])
                    sdessdeg = lauxi001[7] if lauxi001[7] != None else ''
                    sdessdes = lauxi001[8] if lauxi001[8] != None else ''
                    sdessded = lauxi001[9] if lauxi001[9] != None else ''
                    snomeure = lauxi001[10]
                    sdtliber = abnf_converte_datahora(lauxi001[11], 1)
                    sdescrli = lauxi001[12] if lauxi001[12] != None else ''
                    iidcusli = lauxi001[13]
                    snomeuli = lauxi001[14] if lauxi001[14] != None else 'LIBERADO PELO SISTEMA' if iidcusli != None and iidcusli == 0 else ''
                    abnf_imprime_info_001(sarquwri, None, None, 1,
                        [
                            (sdataage, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (hseghage, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (scodctrl, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (sprefvei, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (sdtreten, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (sdescrre, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sstatret, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sdessdeg, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sdessdes, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sdessded, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (snomeure, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (sdtliber, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            (sdescrli, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                            (snomeuli, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                abnf_imprime_line(sarquwri, icolspan, 'black')
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        ('Total de retenções impressas:', icolspan - 1, 0, None, 'Left'  , 'black', 'Courier New', ifontlen, True, False),
                        (icontreg,                                   1, 0, None, 'Right' , 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
            elif irelator == 11:
                # /////////////////////////
                # 11 - DIÁRIO DA MANUTENÇÃO
                # /////////////////////////
                abnf_imprime_fthead_tbody(sarquwri)
                # //////////////////////////////////////////////////////
                # Filtrando registros de renteção de veículos do período
                # //////////////////////////////////////////////////////
                sauxi001 = 'SELECT '
                # Campos das tabelas
                sauxi001 = sauxi001 + 'abnf01.dataage, '    # [00] Data do agendamento
                sauxi001 = sauxi001 + 'abnf01.seghage, '    # [01] Hora do agendamento
                sauxi001 = sauxi001 + 'abnf01.codctrl, '    # [02] Código de controle
                sauxi001 = sauxi001 + 'abnf02.prefvei, '    # [03] Prefixo do veículo
                sauxi001 = sauxi001 + 'abnf01.dtreten, '    # [04] Data/hora da retenção
                sauxi001 = sauxi001 + 'abnf01.descrre, '    # [05] Motivo da retenção
                sauxi001 = sauxi001 + 'abnf01.statret, '    # [06] Status da retenção
                sauxi001 = sauxi001 + 'abnf07.dessdeg, '    # [07] Descricao do grupo de GSD
                sauxi001 = sauxi001 + 'abnf06.dessdes, '    # [08] Descrição do subgrupo de GSD
                sauxi001 = sauxi001 + 'abnf05.dessded, '    # [09] Descrição da definição de GSD
                sauxi001 = sauxi001 + 'abnf03.nomeusu, '    # [10] Usuário que realizou a retenção
                sauxi001 = sauxi001 + 'abnf01.dtliber, '    # [11] Data/hora da liberação
                sauxi001 = sauxi001 + 'abnf01.descrli, '    # [12] Observação na liberação
                sauxi001 = sauxi001 + 'abnf04.nomeusu  '    # [13] Usuário que realizou a liberação
                # Tabela de retenção
                sauxi001 = sauxi001 + 'FROM abnf_operacional_movimentacao_programacao_retencao_veiculos AS abnf01 '
                # Tabela de veículos
                sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos                                AS abnf02 '
                sauxi001 = sauxi001 + 'ON         abnf01.idveicu = abnf02.idveicu '
                # Tabela de usuário (usuário que reteve)
                sauxi001 = sauxi001 + 'INNER JOIN abnf_sistema_usuarios                                 AS abnf03 '
                sauxi001 = sauxi001 + 'ON         abnf01.idcusre = abnf03.idusuar '
                # Tabela de usuário (usuário que liberou)
                sauxi001 = sauxi001 + 'LEFT JOIN abnf_sistema_usuarios                                  AS abnf04 '
                sauxi001 = sauxi001 + 'ON        abnf01.idcusli = abnf04.idusuar '
                # Tabela definição de GSD
                sauxi001 = sauxi001 + 'LEFT JOIN abnf_sigom_cadastro_defeitos_definicoes                AS abnf05 '
                sauxi001 = sauxi001 + 'ON        abnf01.idsdede = abnf05.idsdede '
                # Tabela de subgrupos de GSD
                sauxi001 = sauxi001 + 'LEFT JOIN abnf_sigom_cadastro_defeitos_subgrupos                 AS abnf06 '
                sauxi001 = sauxi001 + 'ON        abnf05.idsdesg = abnf06.idsdesg '
                # Tabela de grupo de GSD
                sauxi001 = sauxi001 + 'LEFT JOIN abnf_sigom_cadastro_defeitos_grupos                    AS abnf07 '
                sauxi001 = sauxi001 + 'ON        abnf06.idsdegr = abnf07.idsdegr '
                # Cláusula WHERE
                sauxi001 = sauxi001 + 'WHERE '
                sauxi001 = sauxi001 + 'abnf01.idfilia = ' + str(iidfilia) + ' AND '                                                                 # ==> Somente registros da filial
                sauxi001 = sauxi001 + 'abnf01.situreg != "C" AND '                                                                                  # ==> Somente registros não cancelados (retenção)
                sauxi001 = sauxi001 + 'abnf01.dtliber IS NULL AND ('                                                                                # ==> Somente registros não finalizados
                sauxi002 = ''
                if ddats01i != None and ddats01f != None and ddats01i <= ddats01f:
                    sauxi002 = sauxi002 + '(abnf01.statret = 1 AND abnf01.dataage BETWEEN "' + str(ddats01i) + '" AND "' + str(ddats01f) + '")'     # ==> Data de agendamento do status 01
                if ddats02i != None and ddats02f != None and ddats02i <= ddats02f:
                    if sauxi002 != '': sauxi002 = sauxi002 + ' OR '
                    sauxi002 = sauxi002 + '(abnf01.statret = 2 AND abnf01.dataage BETWEEN "' + str(ddats02i) + '" AND "' + str(ddats02f) + '")'     # ==> Data de agendamento do status 02
                if ddats03i != None and ddats03f != None and ddats03i <= ddats03f:
                    if sauxi002 != '': sauxi002 = sauxi002 + ' OR '
                    sauxi002 = sauxi002 + '(abnf01.statret = 3 AND abnf01.dataage BETWEEN "' + str(ddats03i) + '" AND "' + str(ddats03f) + '")'     # ==> Data de agendamento do status 03
                if ddats04i != None and ddats04f != None and ddats04i <= ddats04f:
                    if sauxi002 != '': sauxi002 = sauxi002 + ' OR '
                    sauxi002 = sauxi002 + '(abnf01.statret = 4 AND abnf01.dataage BETWEEN "' + str(ddats04i) + '" AND "' + str(ddats04f) + '")'     # ==> Data de agendamento do status 04
                sauxi002 = sauxi002 + ') '    
                sauxi001 = sauxi001 + sauxi002
                # Ordenação
                # (28/08/2025 - Alterado a busca pela data do agendamento # sauxi001) sauxi001 = sauxi001 + 'ORDER BY abnf01.dtreten, abnf02.prefvei;'
                sauxi001 = sauxi001 + 'ORDER BY abnf01.dataage, abnf01.seghage, abnf02.prefvei;'
                # Execução
                lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                # Debug (início)
                # abnf_show('05', lsqlre01, 1)
                # Debug (fim)
                dstatusr = {
                    1: 'STATUS 01 - PRESO',
                    2: 'STATUS 02 - RETIDO',
                    3: 'STATUS 03 - RETORNO DIARIO',
                    4: 'STATUS 04 - RETORNO NOTURNO',
                }
                ddttmnow = datetime.now()
                for iauxi001 in (1, 2, 3, 4):
                    if   iauxi001 == 1 and bstatu01 == True and ddats01i != None and ddats01f != None and ddats01i <= ddats01f: bvalidad = True
                    elif iauxi001 == 2 and bstatu02 == True and ddats02i != None and ddats02f != None and ddats02i <= ddats02f: bvalidad = True
                    elif iauxi001 == 3 and bstatu03 == True and ddats03i != None and ddats03f != None and ddats03i <= ddats03f: bvalidad = True
                    elif iauxi001 == 4 and bstatu04 == True and ddats04i != None and ddats04f != None and ddats04i <= ddats04f: bvalidad = True
                    else: bvalidad = False
                    if bvalidad:
                        icontreg = 0
                        sauxi001 = dstatusr[iauxi001] + ' - PERÍODO: '
                        if   iauxi001 == 1: sauxi001 = sauxi001 + abnf_converte_data(ddats01i) + ' Á ' + abnf_converte_data(ddats01f)
                        elif iauxi001 == 2: sauxi001 = sauxi001 + abnf_converte_data(ddats02i) + ' Á ' + abnf_converte_data(ddats02f)
                        elif iauxi001 == 3: sauxi001 = sauxi001 + abnf_converte_data(ddats03i) + ' Á ' + abnf_converte_data(ddats03f)
                        elif iauxi001 == 4: sauxi001 = sauxi001 + abnf_converte_data(ddats04i) + ' Á ' + abnf_converte_data(ddats04f)
                        abnf_imprime_line(sarquwri, icolspan, 'black')
                        abnf_imprime_info_001(sarquwri, '#84A5BF', 'center', 1,
                            [
                                (sauxi001, icolspan, 0, None, None, 'black', 'Courier New', ifontlen + 2, True, False),
                            ]
                        )
                        abnf_imprime_info_001(sarquwri, '#BFD5D6', 'center', 1,
                            [
                                ('Agendamento', 4, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                                ('Veículo',     1, 2, None, None, 'black', 'Courier New', ifontlen, True, False),
                                ('Retenção',    6, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )                
                        abnf_imprime_info_001(sarquwri, '#BFD5D6', 'center', 1,
                            [
                                ('Data',        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                                ('Hora',        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                                ('Dias',        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                                ('Controle',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                                ('Data/hora',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                                ('Motivo',      1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                                ('GSD',         3, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                                ('Usuário',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
                        abnf_imprime_line(sarquwri, icolspan, 'black')
                        for lauxi001 in lsqlre01:
                            ddataage = lauxi001[0]
                            iseghage = lauxi001[1]
                            istatret = lauxi001[6]
                            if   ddataage == ddataini and iseghage < ihoraini: bvalidad = False
                            elif ddataage == ddatafim and iseghage > ihorafim: bvalidad = False
                            elif istatret != iauxi001: bvalidad = False
                            else: bvalidad = True
                            if bvalidad:
                                icontreg += 1
                                iqtddias = (ddttmnow.date() - ddataage).days
                                iqtddias = iqtddias if iqtddias > 0 else ''
                                sdataage = abnf_converte_data(ddataage)
                                hseghage = abnf_converte_segundos_em_hora_string(iseghage, False)
                                scodctrl = str(1000000 + lauxi001[2])[1:]
                                sprefvei = lauxi001[3]
                                sdtreten = abnf_converte_datahora(lauxi001[4], 1)
                                sdescrre = lauxi001[5]
                                sdessdeg = lauxi001[7] if lauxi001[7] != None else ''
                                sdessdes = lauxi001[8] if lauxi001[8] != None else ''
                                sdessded = lauxi001[9] if lauxi001[9] != None else ''
                                snomeure = lauxi001[10]
                                abnf_imprime_info_001(sarquwri, None, None, 1,
                                    [
                                        (sdataage, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (hseghage, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (iqtddias, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (scodctrl, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (sprefvei, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (sdtreten, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                        (sdescrre, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                        (sdessdeg, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                        (sdessdes, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                        (sdessded, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                        (snomeure, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                    ]
                                )
                        abnf_imprime_line(sarquwri, icolspan, 'black')
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                ('Total de retenções impressas:', icolspan - 1, 0, None, 'Left'  , 'black', 'Courier New', ifontlen, True, False),
                                (icontreg,                                   1, 0, None, 'Right' , 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
            abnf_imprime_ftbody_ftable_fform_fbody(sarquwri)
        abnf_socket_004([7, sarqurel])
        abnf_socket_004([5, 'btgerrel'])
        abnf_alert('Relatório gerado com sucesso!', 3)
        time.sleep(5)
        abnf_alert('', 0)
                    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
