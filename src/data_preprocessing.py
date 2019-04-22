import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

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

    def dropAColumn(self, col_str=''):
        self.dataframe = self.dataframe.drop(labels= col_str, axis=1);
        return self.dataframe

    def minMaxScaling(self, dataframe  = pd.DataFrame.from_dict({}), y_label= ''):

        if y_label is not '':
            features_df = dataframe.drop(labels=y_label, axis=1);
        else:
            features_df = dataframe;

        array = MinMaxScaler().fit_transform(features_df);
        features_df = pd.DataFrame(data=array, columns=features_df.keys());

        if y_label is not '':
            labels_df = self.dataframe[y_label];
            features_df = pd.concat([features_df, labels_df], axis=1);

        return features_df

    def labelEncoding(self, col_str = ''):             ##To be fixed for tensorflowImplementation
        self.dataframe[col_str] = LabelEncoder().fit_transform(self.dataframe[col_str]);
        return self.dataframe