import pandas as pd
from datetime import datetime
data_hoje = datetime.today().strftime('%d.%m')
print(data_hoje)
caminho = 'C:/Users/Varad/Programming/Magalu/arcadeteste/romaneios'
df_abc = pd.read_csv(f'{caminho}/romaneios abc {data_hoje}.csv', low_memory=False, sep=';', encoding="ISO-8859-1", index_col=False)
df_gru = pd.read_csv(f'{caminho}/romaneios gru {data_hoje}.csv', low_memory=False, sep=';', encoding="ISO-8859-1", index_col=False)
df_osa= pd.read_csv(f'{caminho}/romaneios osa {data_hoje}.csv', low_memory=False, sep=';',  encoding="ISO-8859-1", index_col=False)
df_vgi= pd.read_csv(f'{caminho}/romaneios vgi {data_hoje}.csv', low_memory=False, sep=';',  encoding="ISO-8859-1", index_col=False)

df_concat = pd.concat([df_vgi, df_osa, df_abc, df_gru], ignore_index=True)
df_concat.to_csv(f'C:/Users/Varad/Programming/Magalu/arcadeteste/romaneios/romaneios geral.csv', index=False)

df = pd.read_csv(f'{caminho}/romaneios geral.csv',low_memory=False, sep=',', index_col=False)
df.to_csv(f'C:/Users/Varad/Programming/Magalu/arcadeteste/prioridades {data_hoje}.csv',
             index=False)