# 🚀 Projeto de Controle Operacional e Gestão de Frotas (Real-Time)
Este é um sistema Full-Stack desenvolvido para automatizar e otimizar a escala de veículos, gestão de frotas e comunicação entre os setores de Manutenção e Centro de Controle de Operação (CCO) em empresas de transporte. O projeto foca na eliminação de erros operacionais e na velocidade de decisão através de dados em Tempo Real.

## ✨ Funcionalidades e Impacto
O sistema transforma um processo manual e lento em uma solução instantânea de alta performance.

- **Automação e Escala em Segundos:** Automatiza a complexa escala de veículos, refazendo todo o processo em segundos (anteriormente manual e demorado) sempre que um veículo é liberado ou retido pela manutenção.

- **Comunicação Real-Time:** Utiliza Flask-SocketIO para garantir a distribuição instantânea de informações críticas (retenções, liberações, novas regras) entre os setores de Manutenção e CCO.

- **Gestão à Vista (Dashboards):** Gera Dashboards dinâmicos (ECharts) que exibem indicadores de frota e operação em tempo real em Smart TVs. Isso permite a tomada de decisões gerenciais de forma imediata.

- **Motor de Regras Complexo:** Implementa um sistema robusto de validação de regras de negócio (portas, ar-condicionado, prioridades de linha), eliminando erros humanos no processo de escalonamento.

## 🛠️ Stack Tecnológica

| Categoria | Detalhes |
| :--- | :--- |
| **Backend & Real-Time** | **Python**, **Flask** (Framework), **Flask-SocketIO** (WebSockets). |
| **Banco de Dados** | **MySQL/MariaDB** (Estrutura de dados e otimização de consultas). |
| **Frontend & Visualização** | **Bootstrap** (Responsividade), **ECharts** (Gráficos e Dashboards), HTML5/CSS3. |
| **Ferramentas** | **Git** (Controle de Versão), **APIs REST** (Comunicação de serviços). |

## ⚙️ Como Rodar o Projeto (Ambiente Local)

Este sistema Full-Stack possui dependências internas complexas, mas o processo básico de configuração para a equipe de desenvolvimento envolve:

1.  **Ambiente Virtual:** Utilização de `venv` ou `conda` para isolamento de dependências.
2.  **Instalação:** Execução de `pip install -r requirements.txt`.
3.  **Configuração do Banco de Dados:** O sistema requer uma instância ativa do **MySQL** e o *import* do esquema de dados.
4.  **Execução:** Inicialização do Flask com as variáveis de ambiente necessárias para o **Flask-SocketIO** e o servidor de *WebSockets*.