#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas


# In[1]:


import pandas 

tabela = pandas.read_csv (r'C:\Users\paula\Downloads\telecom.csv')
tabela = tabela.drop ('Unnamed: 0', axis=1)
tabela ['TotalGasto'] = pandas.to_numeric (tabela['TotalGasto'], errors='coerce')
tabela = tabela.dropna(how='all',axis=1)
tabela = tabela.dropna(how='any', axis=0)

print (tabela.info())
display (tabela)


# In[29]:


print (tabela['Churn'].value_counts())
print (tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))


# In[32]:


import plotly.express as pty


# In[ ]:


import plotly.express as pty

#https://plotly.com/python/histograms/ --> designers e opçoes de grafico
for coluna in tabela.columns:
    grafico = pty.histogram (tabela, x=coluna, color='Churn')
    grafico.show()


# In[ ]:


Conclusão:
    
    Clientes que estão há pouco tempo estão cancelando muito:
     - Podemos oferecer promoção para assinantes novos.
     - Primeira impressão pode estar sendo confusa.
     - Criar incentivos para os assinantes com contratos fidelidade.
     - Primeira experiência talvez esteja desagradando.
    Boletos eletrônicos tem mais taxa de cancelamento:
     - Dar desconto em pagamentos no cartão/débito automático.
    Anuidades/Mensalidades:
     - Oferecer regalías para clientes com contratos anuais.
    Serviços Combo cancelam menos:
     - Oferecer serviços extra com desconto alto.
    Clientes com dependentes e/ou casados cancelam menos:
     - Promoções em serviços de família.
     - Segunda linha grátis ou com alto desconto.

