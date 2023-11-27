import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

sns.set_theme() 

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Estudo de Previsão de Renda",
     page_icon="https://static.vecteezy.com/ti/vetor-gratis/t2/27196265-lucro-e-renda-previsao-conceito-o-negocio-ou-investimento-oportunidade-e-mercado-predicao-futuro-crescimento-ou-carreira-desenvolvimento-visao-mulher-escalada-seta-com-grande-telescopio-binoculos-vetor.jpg",
     layout="wide",
)

primaryColor="#080707"
backgroundColor="#aec1ea"
secondaryBackgroundColor="#06025a"
textColor="#f9f5f5"
font="serif"

st.title(' Análise exploratória da previsão de renda')

st.header('Estudo da análise exploratória da previsão de renda, exercicío do Modulo 16 do Curso de Cientista de Dados da EBAC.')

st.subheader('Para maiores informações, por favor visite o estudo completo no [Repositório da Aluna Bélit]("https://github.com/belitberno/TdD_IV_Previsao_de_Renda-").')

col1, col2, col3 = st.columns(3)
with col1:
   st.header("")
   st.image("https://static.vecteezy.com/ti/vetor-gratis/t2/7381733-investimento-upside-potencial-economia-previsao-ou-previsao-visao-ou-analisar-futuro-negocio-crescimento-ou-ganhar-aumento-conceito-empresario-olhar-atraves-telescopio-para-ver-investimento-crescimento-grafico-vetor.jpg")
with col2:
   st.header("")
   st.image("https://static.vecteezy.com/ti/vetor-gratis/t2/16247930-crescimento-dos-negocios-aumento-do-lucro-do-investimento-crescimento-rapido-ou-melhoria-de-vendas-e-receita-conceito-de-progresso-ou-desenvolvimento-empresario-montando-foguete-no-grafico-de-barras-de-crescimento-ou-subindo-o-grafico-de-receita-vetor.jpg")
with col3:
   st.header("")
   st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4iCdOeAmawsTt3y2VgERvtn1ePh1gdS6tF9kfqEfcrjbjx3X7vYDOPtqiGD2zSLTXFqY&usqp=CAU")


renda = pd.read_csv('.\\input\\previsao_de_renda.csv')
renda.data_ref = pd.to_datetime(renda.data_ref)

min_data = renda.data_ref.min()
max_data = renda.data_ref.max()

st.write(min_data)
st.write(max_data)

data_inicial = st.sidebar.date_input('Data inicial', 
                value = min_data,
                min_value = min_data,
                max_value = max_data)
data_final = st.sidebar.date_input('Data inicial', 
                value = max_data,
                min_value = min_data,
                max_value = max_data)    

st.sidebar.write('Data inicial = ', data_inicial)
st.sidebar.write('Data inicial = ', data_final)

renda  = renda[(renda['data_ref'] <= pd.to_datetime(data_final)) & (renda['data_ref'] >=pd.to_datetime(data_inicial) )]
#plots
fig, ax = plt.subplots(8,1,figsize=(10,70))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')
sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(7,1,figsize=(10,50))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
sns.despine()
st.pyplot(plt)


