import pandas as pd
import pickle as pk

def saveDf(filename:str, df:pd.DataFrame) -> None:
    df.to_csv(filename + '.csv')

    return  None

def openDf(filename:str, ind_c = True) -> pd.DataFrame:
    if ind_c:
        df = pd.read_csv(filename + '.csv', index_col='Unnamed: 0')
    else:
        df = pd.read_csv(filename + '.csv')

    return df

def openPk(filename:str):
    with open(filename, 'rb') as f:
        return pk.load(f)

def savePk(filename:str, var):
    with open(filename, 'wb') as f:
        pk.dump(var, f)

    return None
