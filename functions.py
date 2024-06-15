##Function to have % of missing data

def nulls(df):
    import pandas as pd
    nulls_percent_df = pd.DataFrame(df.isna().sum()/len(df)).reset_index()
    nulls_percent_df.columns = ['column_name', 'nulls_percentage']
    return (nulls_percent_df)


##Function to rename variables

def minusculas(df):
    for column in df.columns:
        df.columns = [x.lower() for x in df.columns]
    