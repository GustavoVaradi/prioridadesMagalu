# encoding='ISO-8859-1', index_col=False

import pandas as pd
import streamlit as st
#import plotly.express as px



st.set_page_config(layout="wide")
#decimal=","
df = pd.read_csv("prioridades.csv", encoding="ISO-8859-1",
                  index_col=False, sep=";")

df["Nro. Entrega"] = df["Nro. Entrega"].astype(object)
df['Numero End. Pessoa Visita'] = df['Numero End. Pessoa Visita'].astype(object)

# Nro. Entrega | Sigla Unidade Atual | 
# (Logradouro Pessoa Visita + Numero End. Pessoa Visita) |
# Valor Total | Status 

def transform_string(s):
    changed = s.replace('R$', '').replace('.','').replace(',','.')
    return float(changed)

df['Valor Total'] = df['Valor Total'].apply(transform_string)

endereco = df['Logradouro Pessoa Visita'] + ' - nº ' +df['Numero End. Pessoa Visita'].astype(str)

data = {'Entrega': df["Nro. Entrega"],
        'Unidade': df["Sigla Unidade Atual"],
        'Endereco': endereco,
        'Valor Total': df["Valor Total"],
        'Status': df['Status'],
        'Motorista': df['Ult. Motorista']
        }

# Novo DataFrame
df_novo = pd.DataFrame(data)

df_novo = df_novo[(df_novo['Valor Total']>=3000)]
df_novo['Status'].loc[~df_novo['Status'].isin(['EM ROTA', 'ENTREGUE'])] = 'NÃO ROTEIRIZADO'
# df_novo['Status'].unique()

df_novo = df_novo.sort_values(["Valor Total"], ascending=False)

df_novo['Valor Total'] = df_novo['Valor Total'].apply(lambda x: f'R${x:,.2f}')

df_novo['Entrega'] = df_novo['Entrega'].astype(str)

status = st.sidebar.selectbox("Status", df_novo['Status'].unique())
unidade = st.sidebar.selectbox("Base", df_novo['Unidade'].unique())

unidade_filtro = ['GRU', 'VGI', 'ABC', 'OSA']
status_filtro = ['ENTREGUE', 'EM ROTA', 'NÃO ROTEIRIZADO']

df_novo = df_novo[df_novo['Status']== status]
df_novo = df_novo[df_novo['Unidade'] == unidade]
df_novo


#adicionar ultimo motorista
