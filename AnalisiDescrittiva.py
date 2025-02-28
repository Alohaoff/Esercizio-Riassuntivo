from DefGenerazione import generadati
import seaborn as sns
import matplotlib.pyplot as plt

def AnalisiDescrittiva():
    
    df_diab, dataset_diab = generadati()
    
    print(df_diab.info())
    print(df_diab.describe())
    
    correlation_matrix = df_diab.select_dtypes(include=["number"]).corr()
    plt.figure(figsize =(10,6))
    sns.heatmap(correlation_matrix, annot = True, cmap ="coolwarm", fmt = ".2f", linewidths =1)
    plt.show()
    