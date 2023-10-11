import pandas as pd
import streamlit as st
from datetime import datetime
#import plotly.express as px

def transform_string(s):
    changed = s.replace('R$', '').replace('.','').replace(',','.')
    return float(changed)

st.set_page_config(layout="wide")

data_hoje = datetime.today().strftime('%d.%m')
df = pd.read_csv(f"prioridades {data_hoje}.csv", index_col=False, sep=",")

df["Nro. Entrega"] = df["Nro. Entrega"].astype(object)
df = df.drop_duplicates(subset=['Nro. Entrega'])
df['Numero End. Pessoa Visita'] = df['Numero End. Pessoa Visita'].astype(object)
df['Valor Total'] = df['Valor Total'].apply(transform_string)
endereco = df['Logradouro Pessoa Visita'] + ' - nº ' +df['Numero End. Pessoa Visita'].astype(str)

unidades_atuais = ['GRU', 'VGI', 'ABC', 'OSA']
df = df[df['Sigla Unidade Atual'].isin(unidades_atuais)]

status_filtro = ['ENTREGUE', 'EM ROTA', 'PENDENTE']
df.loc[~df['Status'].isin(status_filtro), 'Status'] = 'NÃO ROTEIRIZADO'

# (Logradouro Pessoa Visita + Numero End. Pessoa Visita)
# Valor Total | Status  | Nro. Entrega | Sigla Unidade Atual |

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

df_novo.to_csv('C:/Users/Varad/Programming/Magalu/arcadeteste/prioridades/prioridades.csv', index=False)

df_novo = df_novo.sort_values(["Valor Total"], ascending=False)

df_novo['Valor Total'] = df_novo['Valor Total'].apply(lambda x: f'R${x:,.2f}')

df_novo['Entrega'] = df_novo['Entrega'].astype(str)

status = st.sidebar.selectbox("Status", df_novo['Status'].unique())
unidade = st.sidebar.selectbox("Base", df_novo['Unidade'].unique())


# for i in unidade_filtro:
#     if df_novo['Unidade'].item() == i:
#         df_novo = df_novo[df_novo['Unidade']== i]

df_novo = df_novo[df_novo['Status']== status]
df_novo = df_novo[df_novo['Unidade'] == unidade]
df_novo


#adicionar ultimo motorista
