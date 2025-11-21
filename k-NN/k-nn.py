#######################################################
# Creator: Filipy                                     #
# LinkedIn: Filipy S. Furtado/The most beautiful guy  #
# Instagram: sf.filipy                                #
# Discord: furth__                                    #
#######################################################

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


#kNN stands for: k-Nearest Neighbor
def __init__(self):
    pass


def gender(x):
    if x == 'Female': return 1
    else: return 0


def eletrocardiogram(x):
    if x == 'Normal': return 0
    elif x == 'ST': return 1


def pain(x):
    if x == 'TA': return 1
    elif x == 'ATA': return 2
    elif x == 'NAP': return 3
    else: return 0


def angina(x):
    if x == 'Y': return 1
    else: return 0


def slope(x):
    if x == 'Flat': return 1
    else: return 0


with open('heart.csv', 'r') as f:
    df = pd.read_csv(f)
    f.close()

df['ST_Slope'] = df['ST_Slope'].apply(slope)
df['ExerciseAngina'] = df['ExerciseAngina'].apply(angina)
df['ChestPainType'] = df['ChestPainType'].apply(pain)
df['Sex'] = df['Sex'].apply(gender)
df['RestingECG'] = df['RestingECG'].apply(eletrocardiogram)

df_dp = df['HeartDisease']
df = df.drop('HeartDisease', axis=1)

