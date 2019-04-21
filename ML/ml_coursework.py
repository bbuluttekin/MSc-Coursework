import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder, MinMaxScaler, StandardScaler, MaxAbsScaler
from sklearn.model_selection import StratifiedKFold, GridSearchCV, cross_val_score, cross_val_predict
from sklearn.svm import LinearSVC, SVC
from sklearn.metrics import auc, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score, roc_curve
from sklearn.base import clone
from imblearn.pipeline import make_pipeline
from imblearn.under_sampling import CondensedNearestNeighbour, NeighbourhoodCleaningRule, RandomUnderSampler
from imblearn.metrics import classification_report_imbalanced
from imblearn.over_sampling import RandomOverSampler
from imblearn.ensemble import BalancedRandomForestClassifier, BalancedBaggingClassifier, EasyEnsembleClassifier
import warnings
warnings.filterwarnings(action='ignore')


RANDOM_STATE = 123

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/yeast/yeast.data"
columns = ["mcg", "gvh", "alm", "mit", "erl", "pox", "vac", "nuc", "class"]

df = pd.read_csv(url, header=None, sep=r"\s+",
                 names=columns, usecols=list(range(1, 10)))


def process_data(df):
    encoder = LabelEncoder()
    y = encoder.fit_transform(df['class'])
    X = df[df.columns[:-1]].values
    return X, y


def process_scaled_data(df):
    l_encoder = LabelEncoder()
    scaler = MinMaxScaler()
    y = l_encoder.fit_transform(df['class'])
    X = df[df.columns[:-1]].values
    X = scaler.fit_transform(X)
    return X, y


def make_over_sample(X, y, random_state=0):
    ros = RandomOverSampler(random_state=random_state)
    return ros.fit_resample(X, y)


def make_under_sample(X, y, method=NeighbourhoodCleaningRule, random_state=0):
    clf = method(random_state=random_state)
    return clf.fit_resample(X, y)
