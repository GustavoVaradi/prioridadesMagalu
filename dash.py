import pandas as pd
import streamlit as st
from datetime import datetime

data_hoje = datetime.today().strftime('%d.%m')
print(datetime.today().strftime('%d/%m/%Y - %H:%M:%S'))
caminho = 'C:/Users/Varad/Programming/Magalu/arcadeteste/romaneios'

df_romaneios = pd.read_csv(f'{caminho}/romaneios.csv', low_memory=False, sep=';',  encoding="ISO-8859-1", index_col=False)
df_carga = pd.read_csv(f'{caminho}/carga.csv', low_memory=False, sep=';',  encoding="ISO-8859-1", index_col=False)
pd.concat([df_romaneios, df_carga], ignore_index=True).to_csv(f'romaneios/romaneios geral.csv', index=False)
# df_concat.to_csv(f'C:/Users/Varad/Programming/Magalu/arcadeteste/romaneios/romaneios geral.csv', index=False)

def transform_string(s):
    changed = s.replace('R$', '').replace('.','').replace(',','.')
    return float(changed)

st.set_page_config(layout="wide")

data_hoje = datetime.today().strftime('%d.%m')

df = pd.read_csv('romaneios/romaneios geral.csv',low_memory=False, sep=',', index_col=False)

df["Nro. Entrega"] = df["Nro. Entrega"].astype(object)
df = df.drop_duplicates(subset=['Nro. Entrega'])
df['Numero End. Pessoa Visita'] = df['Numero End. Pessoa Visita'].astype(object)
df['Valor Total'] = df['Valor Total'].apply(transform_string)
endereco = df['Logradouro Pessoa Visita'] + ' - nº ' + df['Numero End. Pessoa Visita'].astype(str)

unidades_atuais = ['HGRU', 'HVGI', 'HABC', 'OSA']
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
#df_concat.to_csv(f'C:/Users/Varad/Programming/Magalu/arcadeteste/romaneios/romaneios geral.csv', index=False)

#df_novo.to_csv(f'romaneios/prioridades {data_hoje}.csv')
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
