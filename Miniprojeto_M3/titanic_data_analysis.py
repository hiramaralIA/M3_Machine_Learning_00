# -*- coding: utf-8 -*-
"""titanic_data_analysis.ipynb
"""

from google.colab import files
import io

import numpy as np 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega arquivo no Colab - conjunto de treinamento dados Titanic

uploaded = files.upload()

# Ler arquivo carregado para no Colab

df = pd.read_csv(io.BytesIO(uploaded['train.csv']))

# Saber informações gerais do nosso banco de dados

df.info()

# Observar as 3 primeiras linhas do conjunto de dados

df.head(3)

# Estatística descritiva dos dados

df.describe()

# Avaliar quantos valores faltantes existem 

df.isnull().sum()

# Preencher valores faltantes com a média

df.fillna(df['Age'].dropna().median(), inplace = True)

df.isnull().sum()

# Saber a dimensão dos dados

df.shape

# Plotar sobreviventes

df.plot(kind = "scatter", x = "Fare", y = "Survived", color = "r", linewidth = 1)
plt.show()

# Sobreviventes em relação a classe do navio (titanic)

sns.barplot(x = "Pclass", y = "Survived", data = df)

# Sobreviventes em realção ao sexo

sns.barplot(x = "Sex", y = "Survived", data = df)

# Informações de Idade e Sexo

survived = 'survived'
not_survived = 'not survived'

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 4))
women = df[df['Sex']=='female']
men = df[df['Sex']=='male']

ax = sns.distplot(women[women['Survived']==1].Age.dropna(), bins=18, label = survived, ax = axes[0], kde =False)
ax = sns.distplot(women[women['Survived']==0].Age.dropna(), bins=40, label = not_survived, ax = axes[0], kde =False)
ax.legend()

ax.set_title('Female')
ax = sns.distplot(men[men['Survived']==1].Age.dropna(), bins=18, label = survived, ax = axes[1], kde = False)
ax = sns.distplot(men[men['Survived']==0].Age.dropna(), bins=40, label = not_survived, ax = axes[1], kde = False)
ax.legend()

_ = ax.set_title('Male')





# Referência:

# https://www.kaggle.com/samukaunt/titanic-passo-a-passo-com-8-modelos-ml-pt-br