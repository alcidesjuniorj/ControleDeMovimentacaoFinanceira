# ControleDeMovimentacaoFinanceira
#Projeto de Movimentação financeira feita em Python Puro

O projeto ControleDeMovimentacaoFinanceira é uma aplicação Python para gerenciar contas bancárias, realizar movimentações financeiras, transferências, e visualizar históricos e gráficos de saldos. Ele utiliza SQLModel para persistência de dados em SQLite e matplotlib para geração de gráficos.

##Etapas do Projeto
1. Modelagem dos Dados
Os modelos estão definidos em models.py:
Bancos: Enum com bancos suportados.
Status: Enum para status da conta (Ativo/Inativo).
Conta: Modelo de conta bancária.
Tipos: Enum para tipo de movimentação (Entrada/Saída).
Historico: Modelo para registrar movimentações financeiras.
O banco de dados SQLite é criado automaticamente ao rodar o projeto.

2. Lógica de Negócio
As funções principais estão em views.py:
criar_conta: Cria uma nova conta bancária.
listar_contas: Lista todas as contas.
desativar_conta: Desativa uma conta (se saldo for zero).
ativar_conta: Ativa uma conta com depósito inicial.
transferir_saldo: Transfere saldo entre contas.
movimentar_dinheiro: Registra entradas/saídas em uma conta.
total_contas: Soma o saldo de todas as contas.
buscar_historicos_entre_datas: Filtra movimentações por data.
criar_grafico_por_conta: Gera gráfico de saldos por banco.

3. Interface do Usuário
A interface de linha de comando está em template.py na classe UI:
Menu interativo para acessar todas as funcionalidades.
Permite criar/desativar contas, transferir, movimentar dinheiro, consultar totais, filtrar históricos e gerar gráficos.

4. Execução
Para iniciar o sistema, execute template.py.
O usuário interage pelo terminal, escolhendo opções do menu.

Como Executar:
Instale as dependências:
pip install sqlmodel matplotlib

Execute o arquivo principal:
python template.py

Observações
O banco de dados é salvo no arquivo database.db.
O projeto é modular, facilitando manutenção e expansão.
Para customizar bancos ou tipos, edite os Enums em models.py.
