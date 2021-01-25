import pandas as pd
from sklearn import model_selection

if __name__ == "__main__":
    df =  pd.read_table("inputs/XYZCorp_LendingData.txt", low_memory=False)

    # shuffling data
    df = df.sample(frac=1).reset_index(drop=True)

    # target columns
    y = df.default_ind.values

    kf = model_selection.StratifiedKFold(n_splits=5)

    for f, (t_, v_) in enumerate(kf.split(X=df, y=y)):
        df.loc[v_, 'kfold'] = f
        
    df.to_csv('inputs/credit_fold.csv', index=False)