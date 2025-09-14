import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame):
    
    df = df.drop_duplicates().reset_index(drop=True)

    df['Postal Code'] = df['Postal Code'].fillna("Unknown")
    df['County'] = df['County'].fillna("Unknown")
    df['City'] = df['City'].fillna("Unknown")
    df['Electric Range'] = df['Electric Range'].fillna(df['Electric Range'].median())
    df['Base MSRP'] = df['Base MSRP'].fillna(0)
    df['Legislative District'] = df['Legislative District'].fillna(df['Legislative District'].median())
    df['Vehicle Location'] = df['Vehicle Location'].fillna(df['City'])
    df['Electric Utility'] = df['Electric Utility'].fillna("Unknown")
    df['2020 Census Tract'] = df['2020 Census Tract'].fillna("Unknown")
    
    return df