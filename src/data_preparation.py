import tensorflow as tf
import pandas as pd
import numpy as np

##Class Name  : ReadDataset
##Description : This class can be used to read the datasets enclosed in various types of source files, every function stores the pandas data frame
##              for further processing

class ReadDataset():
    def __init__(self, filepath):
        self.filepath = filepath
        return

    def readFromCSV(self):
        self.dataframe = pd.read_csv(self.filepath)
        return

    def readFromExcel(self):
        self.dataframe = pd.read_excel(self.filepath)
        return

    def readFromJSON(self):
        self.dataframe = pd.read_json(self.filepath)
        return