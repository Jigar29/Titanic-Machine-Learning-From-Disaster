import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

class DaraPreprocessing():
    def __init__(self, dataframe = {}, tensor = []):
        self.dataframe = pd.DataFrame.from_dict(dataframe);
        self.tensor = tensor;
        return

    def dropNA(self):
        self.dataframe = self.dataframe.dropna(axis=0);
        return self.dataframe

    def dropAnEntry(self, col_str=''):          ##To be fixed
        self.dataframe = self.dataframe.drop(labels= col_str, axis=0);
        return self.dataframe

    def dropAColumn(self, col_str=''):
        self.dataframe = self.dataframe.drop(labels= col_str, axis=1);
        return self.dataframe

    def minMaxScaling(self, y_label= ''):
        scaled_array = MinMaxScaler().fit_transform(X=self.dataframe.drop(labels= y_label, axis=1));
        return scaled_array

    def labelEncoding(self, col_str = ''):             ##To be fixed for tensorflowImplementation
        self.dataframe[col_str] = LabelEncoder().fit_transform(self.dataframe[col_str]);
        return self.dataframe;