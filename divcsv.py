import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

if not os.path.exists("exp_isp_sz_demografia_pow_6.csv"):
    print("Plik CSV nie istnieje")
    exit()

try:
    df = pd.read_csv("exp_isp_sz_demografia_pow_6.csv")

    if 'Liczba mężczyzn' not in df.columns or 'Liczba kobiet' not in df.columns:
        print("Brak wymaganych kolumn w pliku CSV")
        exit()

    df['Suma'] = df['Liczba mężczyzn'] + df['Liczba kobiet']

    df.plot(kind='bar', x='Suma', y=['Liczba mężczyzn', 'Liczba kobiet'])

    plt.show()

except Exception as e:
    print("Wystąpił błąd:", e)