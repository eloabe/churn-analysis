# Análise de Churn

## Tabela de conteúdos
1. [Descrição do projeto](#descricao-projeto)
2. [Demonstração de utilização do web app](#demonstracao-webapp)

   2.1. [Etapa de cadastro](#cadastro)
   
   2.2. [Etapa de previsão](#previsao)
3. [Descrição dos arquivos do projeto](#descricao-arquivos)


<a name="descricao-projeto"></a>
## 1. Descrição do projeto
Nesse projeto, foi explorada a base de dados Telco Customer Churn, de uma competição do Kaggle, que consiste na representação de uma empresa de telefonia que, baseada em dados sobre seus clientes, busca entender o comportamento dos que realizam Churn (cancelamento do serviço). 

Disponível em https://www.kaggle.com/datasets/blastchar/telco-customer-churn

O objetivo do projeto foi praticar **análise exploratória e modelagem de dados**. 

Também foi criada uma aplicação que mostra um uso prático do modelo de Machine Learning utilizado, que consiste na simulação do cadastro de um novo cliente na base de dados para prever qual sua probabilidade de realizar Churn, o que pode ser utilizado para tomar decisões como direcionamento de campanhas de Marketing, promoções, entre outras. Utilizei a biblioteca Streamlit.

<a name="demonstracao-webapp"></a>
## 2. Demonstração de utilização do web app

Disponível em: https://churn-analysis-eloabe.streamlit.app/</a>

<a name="cadastro"></a>
### 2.1. Etapa de cadastro
![Cadastro](https://i.ibb.co/kcMc0Bt/churn-cadastro.png)

<a name="previsao"></a>
### 2.2. Etapa de previsão
![Previsão](https://i.ibb.co/qR6HBCp/churn-previsao.png)

<a name="descricao-arquivos"></a>
## 3. Arquivos do projeto
- **requirements.txt:** lista de bibliotecas Python utilizadas
- **classification.ipynb:** notebook com as análises e modelagem realizadas
- **data/churn.csv:** base de dados utilizada
- **webapp/finalized_model.sav:** arquivo que contém o modelo treinado
- **webapp/previsao_churn.py:** web app que realiza a previsão do novo cliente
