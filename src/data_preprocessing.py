import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, LabelEncoder

class DataPreprocessing():
    def __init__(self, dataframe = {}, tensor = []):
        self.dataframe = pd.DataFrame.from_dict(dataframe);
        self.tensor = tensor;
        return

    def dropNA(self):
        self.dataframe = self.dataframe.dropna(axis=0).reset_index(drop=True);
        return self.dataframe

    def dropAnEntry(self, col_str=''):          ##To be fixed
        self.dataframe = self.dataframe.drop(labels= col_str, axis=0).reset_index(drop=True);
        return self.dataframe

    def dropColumns(self, col_list=''):
        self.dataframe = self.dataframe.drop(labels= col_list, axis=1);
        return self.dataframe

    def oneHotEncoding(self, col_list):
        for col in col_list:
            temp_dataframe = pd.get_dummies(self.dataframe[col])
            self.dataframe = self.dropColumns(col_list=col)
            self.dataframe = self.dataframe.join(temp_dataframe)
        return self.dataframe

    def minMaxScaling(self, dataframe=pd.DataFrame.from_dict({})):
        array = MinMaxScaler().fit_transform(dataframe);
        dataframe = pd.DataFrame(data=array, columns=dataframe.columns);
        return dataframe
