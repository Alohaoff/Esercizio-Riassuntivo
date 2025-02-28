from sklearn.datasets import load_diabetes
import pandas as pd

def generadati():
    
    dati_diab = load_diabetes()
    x = dati_diab.data
    y = dati_diab.target
    df_diab = pd.DataFrame(x, columns=dati_diab.feature_names)
    df_diab['target'] = y
    print("Database creato, prime 5 righe:")
    print(df_diab.head())

    return df_diab, dati_diab