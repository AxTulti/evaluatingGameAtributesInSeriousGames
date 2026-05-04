#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np


# ### Data Path

# In[47]:


DATA_PATH = './data/data.xlsx'

df_raw = pd.read_excel(DATA_PATH)
df = df_raw.copy()


# # Preprocessing of Data

# ## Remove Non-numerical Features
# Since those are only used for segmentation

# In[48]:


df = df.iloc[:, 23:50]


# In[49]:


df


# ## Standarizing column names

# ### We define a column Mapping

# |Spanish Feature Concept      |Parent Category      |Importance Code|Rating Code|
# |-----------------------------|---------------------|---------------|-----------|
# |Desafío                      |Challenge            |CH1            |CH2        |
# |Equilibrio Habilidades/Tareas|Challenge            |CH3            |CH4        |
# |Estructura de Progresión     |Challenge            |CH5            |CH6        |
# |Inmersión                    |Immersion            |I1             |I2         |
# |Involucramiento Emocional    |Immersion            |I3             |I4         |
# |Narrativa Atractiva          |Immersion            |I5             |I6         |
# |Animación y Sonido           |Immersion            |I7             |I8         |
# |Concentración                |Concentration        |C1             |C2         |
# |Claridad de Objetivos        |Goal Clarity         |G1             |G2         |
# |Retroalimentación            |Feedback             |F1             |F2         |
# |Autonomía                    |Autonomy             |A1             |A2         |
# |Interacción Social           |Social Interaction   |S1             |S2         |
# |Mejora del Conocimiento      |Knowledge Improvement|K1             |K2         |
# |Calificación Global          |Overall              |O1             |—          |

# In[50]:


old_cols = list(df.columns)
new_cols = [
    'CH1', 'CH2',  # Desafío
    'F1', 'F2',    # Retroalimentación
    'I1', 'I2',    # Inmersión
    'C1', 'C2',    # Concentración
    'G1', 'G2',    # Claridad de Objetivos
    'A1', 'A2',    # Autonomía
    'S1', 'S2',    # Interacción Social
    'K1', 'K2',    # Mejora del Conocimiento
    'I3', 'I4',    # Involucramiento Emocional
    'CH3', 'CH4',  # Equilibrio entre Habilidades y Tareas
    'I5', 'I6',    # Narrativa Atractiva
    'CH5', 'CH6',  # Estructura de Progresión
    'I7', 'I8',    # Animación y Sonido
    'O1'           # Calificación Global
]
normalization_mapping = dict(zip(old_cols, new_cols))


# In[51]:


df.columns = [normalization_mapping.get(c) for c in df.columns]


# ## Handling Missing Values TODO

# In[53]:


df.isna().sum()


# We will fill missing values with each column's median

# In[54]:


df = df.fillna(df.median())


# In[56]:


df.isna().sum()

