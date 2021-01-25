# lbl_xgb.py

import xgboost as xgb
import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
from sklearn import ensemble

def run(fold):
    df = pd.read_csv('inputs/credit_fold.csv', low_memory=False)
    # dropping missing values columns
    df = df.dropna(axis=1)

    # dropping features with more then 10 categories
    to_drop = [
        'sub_grade',
        'zip_code',
        'addr_state',
        'earliest_cr_line',
        ]
    df = df.drop(to_drop, axis=1)

    features = [f for f in df.columns if f not in ('kfold','default_ind')]

    for col in features:
        encoder = preprocessing.LabelEncoder()
        encoder.fit(df[col])
        df.loc[:, col] = encoder.transform(df[col])
        
    df_train = df[df.kfold != fold].reset_index(drop=True)
    df_valid = df[df.kfold == fold].reset_index(drop=True)
    
    x_train = df_train[features]
    x_valid = df_valid[features]
    
    model = xgb.XGBClassifier(n_jobs=-1)
    model.fit(x_train, df_train.default_ind.values)
    
    valid_preds = model.predict_proba(x_valid)[:,1]
    auc = metrics.roc_auc_score(df_valid.default_ind.values, valid_preds)
    prediction = model.predict(x_valid)
    f1_score = metrics.f1_score(df_valid.default_ind.values, prediction)
    
    print(f"Fold = {fold}, AUC = {auc}, F1 Score = {f1_score}")

if __name__=="__main__":
    for fold in range(5):
        run(fold)