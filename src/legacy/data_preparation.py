import tensorflow as tf
import pandas as pd

class Datapreparation(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.dataframe = pd.DataFrame()
        return

    '''Fuction to create the pandas dataframe from CSV File'''
    def createDataFrameFromCSVFile(self):
        if (self.dataframe.empty):
            self.dataframe = pd.read_csv(self.filepath)
        else:
            print("The DataFrame is already created")

        return

    '''Fuction to create the pandas dataframe from Excel File'''
    def createDataFrameFromExcelFile(self):
        if(self.dataframe.empty):
            self.dataframe = pd.read_excel(self.filepath)
        else:
            print("The DataFrame is already created")

        return

    '''Fuction to create the tensor object from Excel File'''
    def createTensorObjectFromCSVFile(self):
        self.tensor = tf.read_file(self.filepath, "Data_Tensor")
        return

    def createTensorObjectFromExcelFile(self):
        self.tensor = tf.read_file(self.filepath, "Data_Tensor")
        return
