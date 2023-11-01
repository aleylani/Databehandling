# Välkommen till din .py-fil med nyttiga funktioer
# genom att spara användbara funktioner här kan du enkelt importera och återanvända dem


def find_columns_with_nulls_and_plot_v1(df):

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    import warnings
    warnings.filterwarnings('ignore') # obs, detta kommando förtrycker olika varning som dyker upp så att vi slipper se dem 
                                      # i detta fall påverkas endast de varningar som uppstår när vi plottar med Seaborn

    for column in df.columns:         # iterera över alla kolumner i vår dataframe

        if df[column].isnull().sum() > 0:
        
            sns.histplot(df, x=column)
            plt.show()


def find_columns_with_nulls_and_plot_v2(df):

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    import warnings
    warnings.filterwarnings('ignore') # obs, detta kommando förtrycker olika varning som dyker upp så att vi slipper se dem 
                                      # i detta fall påverkas endast de varningar som uppstår när vi plottar med Seaborn

    my_null_series = df.isnull().sum() # notera att detta nu är en Serie 

    columns = my_null_series.index
    values = my_null_series.values

    for col, val in zip(columns, values):

        if val > 0:
            sns.histplot(df, x=col)
            plt.show()