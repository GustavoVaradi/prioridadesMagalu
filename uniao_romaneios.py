import pandas as pd
from datetime import datetime
data_hoje = datetime.today().strftime('%d.%m')
print(data_hoje)


df_abc = pd.read_csv(f'romaneios/romaneios abc {data_hoje}.csv', low_memory=False, sep=';', encoding="ISO-8859-1", index_col=False)
df_gru = pd.read_csv(f'romaneios/romaneios gru {data_hoje}.csv', low_memory=False, sep=';', encoding="ISO-8859-1", index_col=False)
df_osa= pd.read_csv(f'romaneios/romaneios osa {data_hoje}.csv', low_memory=False, sep=';',  encoding="ISO-8859-1", index_col=False)
df_vgi= pd.read_csv(f'romaneios/romaneios vgi {data_hoje}.csv', low_memory=False, sep=';',  encoding="ISO-8859-1", index_col=False)

df_concat = pd.concat([df_vgi, df_abc, df_gru, df_osa], ignore_index=True)
df = pd.read_csv('romaneios/romaneios geral.csv',low_memory=False, sep=';',  encoding="ISO-8859-1", index_col=False)
df.to_csv(f'C:/Users/Varad/Programming/Magalu/arcadeteste/prioridades {data_hoje}.csv',
             index=False)