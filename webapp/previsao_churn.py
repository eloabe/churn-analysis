import os
import pickle

import numpy as np
import pandas as pd
import streamlit as st

ROOT_DIR = os.path.dirname(__file__)
MODEL_DIR = ROOT_DIR + '/finalized_model.sav'

model = pickle.load(open(MODEL_DIR, 'rb'))
features = model.get_booster().feature_names

st.title('Previsão de Churn')
st.write('Esse aplicativo simula o cadastro de um novo cliente para realizar a previsão de Churn.')

st.subheader('Realizando o cadastro do cliente')

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

# Dataframe vazio com as mesmas colunas da base original
df = pd.DataFrame(columns = features, index = [])

# Criando uma nova amostra com as mesmas colunas do modelo treinado

# Dados demográficos do cliente
df.loc[0, 'gender_Male'] = 1 if gender == 'Masculino' else 0
df.loc[0, 'SeniorCitizen_1'] = 1 if senior else 0
df.loc[0, 'Partner_Yes'] = 1 if partner else 0
df.loc[0, 'Dependents_Yes'] = 1 if dependents else 0

# Serviços contratados
df.loc[0, 'PhoneService_Yes'] = 1 if phone_service else 0

df.loc[0, 'MultipleLines_Yes'] = 1 if multiple_lines == 'Sim' else 0
df.loc[0, 'MultipleLines_No'] = 1 if multiple_lines == 'Não' else 0
df.loc[0, 'MultipleLines_No phone service'] = 1 if multiple_lines == 'Não possui serviço de telefone' else 0

df.loc[0, 'InternetService_DSL'] = 1 if internet_service == 'DSL' else 0
df.loc[0, 'InternetService_Fiber optic'] = 1 if internet_service == 'Fibra ótica' else 0
df.loc[0, 'InternetService_No'] = 1 if internet_service == 'Não possui' else 0

df.loc[0, 'OnlineSecurity_Yes'] = 1 if online_security == 'Sim' else 0
df.loc[0, 'OnlineSecurity_No'] = 1 if online_security == 'Não' else 0
df.loc[0, 'OnlineSecurity_No internet service'] = 1 if online_security == 'Não possui internet' else 0

df.loc[0, 'OnlineBackup_Yes'] = 1 if online_backup == 'Sim' else 0
df.loc[0, 'OnlineBackup_No'] = 1 if online_backup == 'Não' else 0
df.loc[0, 'OnlineBackup_No internet service'] = 1 if online_backup == 'Não possui internet' else 0

df.loc[0, 'DeviceProtection_Yes'] = 1 if device_protection == 'Sim' else 0
df.loc[0, 'DeviceProtection_No'] = 1 if device_protection == 'Não' else 0
df.loc[0, 'DeviceProtection_No internet service'] = 1 if device_protection == 'Não possui internet' else 0

df.loc[0, 'TechSupport_Yes'] = 1 if tech_support == 'Sim' else 0
df.loc[0, 'TechSupport_No'] = 1 if tech_support == 'Não' else 0
df.loc[0, 'TechSupport_No internet service'] = 1 if tech_support == 'Não possui internet' else 0

df.loc[0, 'StreamingTV_Yes'] = 1 if streaming_tv == 'Sim' else 0
df.loc[0, 'StreamingTV_No'] = 1 if streaming_tv == 'Não' else 0
df.loc[0, 'StreamingTV_No internet service'] = 1 if streaming_tv == 'Não possui internet' else 0

df.loc[0, 'StreamingMovies_Yes'] = 1 if streaming_movies == 'Sim' else 0
df.loc[0, 'StreamingMovies_No'] = 1 if streaming_movies == 'Não' else 0
df.loc[0, 'StreamingMovies_No internet service'] = 1 if streaming_movies == 'Não possui internet' else 0

# Conta do cliente
df.loc[0, 'Contract_Month-to-month'] = 1 if contract == 'Mês a mês' else 0
df.loc[0, 'Contract_One year'] = 1 if contract == 'Um ano' else 0
df.loc[0, 'Contract_Two year'] = 1 if contract == 'Dois anos' else 0

df.loc[0, 'PaymentMethod_Electronic check'] = 1 if payment == 'Cheque eletrônico' else 0
df.loc[0, 'PaymentMethod_Mailed check'] = 1 if payment == 'Cheque por e-mail' else 0
df.loc[0, 'PaymentMethod_Credit card (automatic)'] = 1 if payment == 'Cartão de crédito' else 0
df.loc[0, 'PaymentMethod_Bank transfer (automatic)'] = 1 if payment == 'Transferência bancária' else 0

df.loc[0, 'PaperlessBilling_Yes'] = 1 if paperless else 0
df.loc[0, 'tenure'] = int( tenure )
df.loc[0, 'MonthlyCharges'] = monthly_charges
df.loc[0, 'TotalCharges'] = tenure * monthly_charges

# Corrigindo os tipos de dados
df['tenure'] = df['tenure'].astype('int64')
df[['MonthlyCharges', 'TotalCharges']] = df[['MonthlyCharges', 'TotalCharges']].astype('float64')

categoricas = df.select_dtypes(include = object).columns.tolist()
df[categoricas] = df[categoricas].astype('uint8')

prob_class1 = model.predict_proba(df)[:, 1].item() * 100

if st.button('Realizar previsão'):
    st.write(f'O cliente tem aproximadamente {round( prob_class1, 2 )}\%  de chance de cancelar o serviço.')