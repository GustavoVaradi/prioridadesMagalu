import pandas as pd
from datetime import datetime
data_hoje = datetime.today().strftime('%d.%m')
print(data_hoje)
caminho = 'C:/Users/Varad/Programming/Magalu/arcadeteste/romaneios'

df_romaneios = pd.read_csv(f'{caminho}/romaneios.csv', low_memory=False, sep=';',  encoding="ISO-8859-1", index_col=False)
df_carga = pd.read_csv(f'{caminho}/carga.csv', low_memory=False, sep=';',  encoding="ISO-8859-1", index_col=False)
pd.concat([df_romaneios, df_carga], ignore_index=True)
df_concat = pd.concat([df_romaneios, df_carga], ignore_index=True)
# pd.concat([df_romaneios, df_carga], ignore_index=True).to_csv(f'romaneios/romaneios geral.csv', index=False)
df_concat.to_csv(f'C:/Users/Varad/Programming/Magalu/arcadeteste/romaneios/romaneios geral.csv', index=False)

# fazer um while com time 
# cad 5 minutos fazer a mesma função
        