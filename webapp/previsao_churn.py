import os
import pickle

import pandas as pd
import streamlit as st

ROOT_DIR = os.path.dirname(os.getcwd())
MODEL_DIR = ROOT_DIR + '\model\\finalized_model.sav'

model = pickle.load(open(MODEL_DIR, 'rb'))
features = model.get_booster().feature_names

df = pd.DataFrame(columns = features, index = [])

st.title('Previsão de Churn')
st.header('Esse aplicativo simula o cadastro de um novo cliente para realizar a previsão de Churn.')

# Dados demográficos sobre o cliente
st.subheader('Dados demográficos sobre o cliente')
gender = st.selectbox('Gênero', ['Masculino', 'Feminino'])
senior = st.checkbox('Idoso?')
partner = st.checkbox('Possui parceiro?')
dependents = st.checkbox('Possui dependentes?')

# Serviços contratados
st.subheader('Serviços que o cliente possui')
phone_service = st.checkbox('Possui serviço de telefone?')

multiple_lines = st.selectbox('Mais de uma linha de telefone?', 
                              ['Sim', 'Não', 'Não possui serviço de telefone'])

internet_service = st.selectbox('Tipo de internet',
                                ['Fibra ótica', 'DSL', 'Não possui'])

online_security = st.selectbox('Segurança online',
                               ['Sim', 'Não', 'Não possui internet'])

online_backup = st.selectbox('Backup online',
                             ['Sim', 'Não', 'Não possui internet'])

device_protection = st.selectbox('Proteção de dispositivo',
                                 ['Sim', 'Não', 'Não possui internet'])

tech_support = st.selectbox('Suporte de informática',
                            ['Sim', 'Não', 'Não possui internet'])

streaming_tv = st.selectbox('Streaming de TV',
                            ['Sim', 'Não', 'Não possui internet'])

streaming_movies = st.selectbox('Streaming de filmes',
                                ['Sim', 'Não', 'Não possui internet'])

# Conta do cliente
st.subheader('Dados sobre a conta do cliente')
tenure = st.number_input('Cliente há quantos meses?', 0, 100)

contract = st.selectbox('Tipo de contrato',
                        ['Mês a mês', 'Um ano', 'Dois anos'])

payment = st.selectbox('Tipo de pagamento',
                        ['Cheque eletrônico', 'Cheque por e-mail',
                         'Cartão de crédito', 'Transferência bancária'])

paperless = st.checkbox('Pagamento on-line?')
monthly_charges = st.slider('Quanto paga por mês?', 0.0, 150.0)
total_charges = tenure * monthly_charges


